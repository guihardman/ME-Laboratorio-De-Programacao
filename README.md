projeto_rpg/
│
├── README.md                  # Documentação
├── main.py                    # Script principal que inicia tudo
│
└── src/
    ├── __init__.py            
    ├── jogo.py                # Gerenciador de estados (Alterna entre Mapa e Combate)
    │
    ├── modelos/               # Pasta para as Classes e Dados (O "esqueleto" do jogo)
    │   ├── __init__.py
    │   ├── entidades.py       # Classes: Personagem, Inimigo, Party (Atributos: Força, Int, Agi)
    │   ├── habilidades.py     # Dicionários ou Classes de Magias (Elementos) e Ataques
    │   └── itens.py           # Classes de itens consumíveis (Poções, etc.) e Inventário
    │
    ├── sistemas/              # Pasta para as lógicas ativas (O "motor" do jogo)
    │   ├── __init__.py
    │   ├── combate.py         # Fila de iniciativa (Agilidade), turnos, e cálculo de dano
    │   ├── ia_inimiga.py      # Lógica isolada para o inimigo buscar o alvo de menor HP
    │   └── mapa.py            # Lógica da matriz, andar (X, Y), pegar itens do chão e RNG de encontros
    │
    └── utils/                 # Ferramentas gerais
        ├── __init__.py
        ├── interface.py       # Funções para imprimir menus (Atacar, Magia, Defender, Item)
        └── matematica.py      # Rolagens de dados, chance de acerto, cálculos de fraqueza