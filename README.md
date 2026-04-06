projeto_rpg/
│
├── README.md                  # Documentação
├── main.py                    # Script principal que inicia tudo
│
└── src/
    ├── __init__.py
    ├── jogo.py                # Gerenciador principal do jogo e eventos
    │
    ├── modelos/               # Classes e dados base do jogo
    │   ├── __init__.py
    │   ├── entidades.py       # Classes: Personagem, Inimigo, Party
    │   ├── habilidades.py     # Magias, ataques e habilidades
    │   └── itens.py           # Itens consumíveis e inventário
    │
    ├── sistemas/              # Lógicas principais do motor
    │   ├── __init__.py
    │   ├── combate.py         # Sistema de turnos e cálculo de dano
    │   ├── ia_inimiga.py      # IA de decisão dos inimigos
    │   ├── mapa.py            # Movimentação, matriz e eventos
    │   ├── npc.py             # Classe base dos NPCs e memória de diálogo
    │   └── npc_ia.py          # Integração com API Gemini para diálogo inteligente
    │
    └── utils/                 # Ferramentas auxiliares
        ├── __init__.py
        ├── interface.py       # Menus, interface e textos do jogo
        └── matematica.py      # Cálculos, rolagens e probabilidades

        ## Funcionalidades recentes

- Sistema de combate por turnos
- Exploração por mapa
- Eventos aleatórios
- IA inimiga com foco no menor HP
- Integração com API Gemini
- Sistema de NPC inteligente com diálogo dinâmico
- Memória básica de conversas com NPC

- ## Funcionalidades recentes

## Integração com IA

Nesta versão, foi implementada a primeira integração de API de inteligência artificial no projeto.

A funcionalidade adiciona:

- NPC com respostas dinâmicas
- contexto baseado na party atual
- memória das últimas interações
- geração de diálogo utilizando Gemini API

- ### Versão experimental
A integração de IA foi implementada em uma branch separada (`feature/npc-ia`) para testes e evolução futura.
