# DESCRIÇÃO DO PROJETO

Um jogo de RPG (Role-Playing Game) clássico baseado em texto desenvolvido totalmente em Python. Este projeto apresenta mecânicas ricas como exploração de mapas em grid (grade), encontros aleatórios, montagem de equipe (party), e um sistema de combate estratégico por turnos com uma IA inimiga básica.

_________________________________________________________________________________________________________________________

# FUNCIONALIDADES PRINCIPAIS

* **Sistema de Party Dinâmico:** Escolha 3 heróis para formar a sua equipe inicial a partir de um catálogo de classes clássicas (Guerreiro, Mago, Clérigo e Ladino).
* **Exploração de Mapa:** Navegue por uma masmorra 2D (grade) usando controles direcionais. Interaja com o ambiente para encontrar baús ocultos ou a saída, enquanto corre o risco de encontros aleatórios.
* **Combate por Turnos:** * Sistema de iniciativa baseado no atributo `Agilidade` (do mais rápido para o mais lento).
    * Cálculo de dano influenciado por status, defesas, acertos críticos e fraquezas elementais.
    * Efeitos secundários de habilidades (ex: Quebra-Escudos que reduz a defesa inimiga temporariamente).
* **IA Inimiga (Inteligência Artificial):** Os inimigos não atacam apenas aleatoriamente. Eles avaliam as resistências dos heróis (HP + Defesa) para focar nos alvos mais fracos e gerenciam o seu próprio MP para usar magias poderosas.
* **Interface Polida (TUI):** Menus limpos, cabeçalhos em ASCII, limpeza automática da tela e logs de batalha narrativos com emojis para uma experiência de jogo imersiva no terminal.
* **Tratamento de Erros:** O jogo captura exceções e lida com interrupções do usuário (Ctrl+C) sem "crashar" o terminal de forma feia.

_________________________________________________________________________________________________________________________

# MANUAL DE USO

Este jogo roda inteiramente no terminal e aguarda a confirmação do usuário para cada ação. **Lembre-se sempre de pressionar `ENTER` após digitar o seu comando.**

### 1. Início e Montagem da Equipe
Ao executar o `main.py`, o jogo inicia a fase de "Draft". 
* O jogador deve recrutar exatamente **3 heróis** para a sua *Party*.
* O sistema permite equipes repetidas (ex: 3 Magos ou 2 Guerreiros e 1 Clérigo). Escolha com sabedoria, pois a composição dita a sua estratégia para o resto do jogo.

### 2. Exploração do Mapa
A navegação ocorre numa matriz bidimensional (grade). O jogador é representado pela sua visão do cenário.

**Legenda do Mapa:**

| Símbolo | Significado | Comportamento no Sistema |
| :---: | :--- | :--- |
| `#` | **Obstáculo** | Bloqueia o movimento. Bater numa parede consome a ação. |
| `.` | **Caminho Livre** | Permite o avanço. Cada passo rola um "dado invisível" para Encontros Aleatórios. |
| `B` | **Baú** | Interação automática ao entrar na célula. (Expansível para inventário no futuro). |
| `S` | **Saída/Boss** | Objetivo final do mapa. |

**Movimentação:** Digite `W` (Cima), `A` (Esquerda), `S` (Baixo) ou `D` (Direita) e pressione `ENTER`. Maiúsculas ou minúsculas são aceitas pelo sistema.

### 3. Sistema de Combate (Fases do Turno)
Quando um encontro aleatório é acionado, o jogo entra no modo de Combate, que é processado em 5 fases distintas:

1. **Planejamento do Jogador:** O jogador escolhe a ação para cada herói vivo. O estado de "Defesa" do turno anterior é resetado automaticamente.
2. **Planejamento da IA:** Os inimigos decidem os seus alvos (avaliando quem tem menor HP/Defesa) e gerenciam o próprio MP para decidir entre ataques básicos ou magias.
3. **Iniciativa (Ordenação):** O sistema reúne todas as ações planejadas e as ordena com base no atributo **Agilidade** de cada entidade. Quem for mais rápido age primeiro.
4. **Resolução:** O motor de matemática calcula acertos, erros, críticos e fraquezas. Se um alvo morrer antes de receber o ataque, o atacante "perde" a ação batendo no vazio.
5. **Checagem de Vitória/Derrota:** Avalia se todos de um dos lados chegaram a 0 HP.

**Ações de Combate:**

* **[1] Atacar:** Usa ataques físicos que escalam com o atributo `Força`. Alguns ataques (como Quebra-Escudos) aplicam efeitos secundários (*debuffs*) no alvo.
* **[2] Magia:** Consome `MP`. Escala com o atributo `Inteligência`. Magias de cura selecionam automaticamente o aliado com o menor HP. Magias elementais (ex: Fogo) causam **dano em dobro** em inimigos com fraqueza correspondente.
* **[3] Defender:** Uma ação tática crucial. Ignora a fila de iniciativa, é aplicada instantaneamente e dobra a defesa base do herói apenas para aquele turno, mitigando danos pesados.
* **[0] Voltar/Cancelar:** O sistema de menus permite retornar à escolha anterior de forma fluida sem perder o turno.

### 4. Status e Cálculos Matemáticos
A matemática do jogo roda no arquivo `matematica.py`. O dano final é calculado da seguinte forma:
> `Dano Base da Habilidade + (Força ou Inteligência) - Defesa Atual do Alvo`

**Modificadores:**
* **Ataque Crítico:** Rola contra a `chance_critico` da habilidade. Se ocorrer, o dano bruto é duplicado antes da defesa do alvo ser subtraída.
* **Fraqueza Elemental:** Funciona da mesma forma que o crítico, multiplicando o dano se o elemento da magia bater com a `fraqueza` do inimigo.

_________________________________________________________________________________________________________________________

# ESTRUTURA DO PROJETO

O código está organizado seguindo boas práticas de modularização, separando a lógica de negócio da interface e dos sistemas:

RPG-de-Texto_Laboratorio-de-Programacao
/
├── main.py                # Entry Point e tratamento de erros críticos
└── src/
    ├── jogo.py            # Loop principal, seleção de party e integração de sistemas
    ├── modelos/           # Pasta para as Classes e Dados
    │   ├── entidades.py   # Classes base e catálogos
    │   ├── habilidades.py # Classes de Ataques e Magias com suporte a efeitos
    │   └── itens.py       # Itens consumíveis (Poções de Vida/Mana)
    ├── sistemas/          # Pasta para as lógicas ativas
    │   ├── combate.py     # Fluxo de batalha, fila de ações e resolução de turnos
    │   ├── mapa.py        # Lógica da matriz, andar (X, Y), pegar itens do chão e RNG de encontros
    │   └── ia_inimiga.py  # Algoritmos de tomada de decisão dos monstros
    └── utils/             # Ferramentas gerais
        ├── interface.py   # Renderização de UI (Menus, Cabeçalhos, Painéis de Status)
        └── matematica.py  # Cálculos puros de dano, RNG e probabilidades
