"""
Módulo: interface.py
Descrição: Gerencia todos os menus e a exibição de informações no terminal.
Isola a interação com o usuário (prints e inputs) da lógica central do jogo.
"""

import os


def limpar_tela():
    """Limpa o terminal independentemente do sistema operacional."""
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_cabecalho(texto):
    """Cria um cabeçalho padronizado com bordas duplas ASCII."""
    tamanho = 56
    print("╔" + "═" * (tamanho - 2) + "╗")
    print("║" + texto.upper().center(tamanho - 2) + "║")
    print("╚" + "═" * (tamanho - 2) + "╝")


def exibir_status_batalha(party, inimigos):
    """Mostra o HP e MP de todos os envolvidos no combate em formato de painel."""
    tamanho = 56
    exibir_cabecalho("STATUS DA BATALHA")
    
    print(" 🛡️  SUA EQUIPE:")
    for p in party:
        if p.esta_vivo():
            barra_hp = f"HP: {p.hp_atual: >3}/{p.hp_max: <3}"
            barra_mp = f"MP: {p.mp_atual: >2}/{p.mp_max: <2}"
            print(f"  ⯈ {p.nome: <20} │ {barra_hp} │ {barra_mp}")
            
    print("-" * tamanho)
    
    print(" 👹 INIMIGOS:")
    for i in inimigos:
        if i.esta_vivo():
            barra_hp = f"HP: {i.hp_atual: >3}/{i.hp_max: <3}"
            print(f"  ⯈ {i.nome: <20} │ {barra_hp}")
    print("=" * tamanho)


def menu_escolher_acao(personagem):
    """Exibe o menu principal de ações do turno para um personagem."""
    tem_itens = bool(personagem.inventario) if hasattr(personagem, 'inventario') else False
    print(f"\nTurno de {personagem.nome}:")
    print("[1] Atacar")
    print("[2] Magia")
    print("[3] Defender")
    print("[4] Usar Item")
    
    while True:
        try:
            escolha = int(input("\nO que fazer? ⯈ "))
            if escolha in [1, 2, 3, 4]:
                return escolha
            print("❌ Opção inválida! Escolha um número de 1 a 4.")
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números.")


def menu_escolher_ataque(personagem):
    """Exibe a lista de ataques físicos do personagem."""
    limpar_tela()
    exibir_cabecalho("ESCOLHER ATAQUE")
    print(f"\nAtaques de {personagem.nome}:")
    
    for i, ataque in enumerate(personagem.ataques):
        print(f"[{i+1}] {ataque.nome} (Poder: {ataque.poder_base})")
        print(f"     └ {ataque.descricao}")
    print("\n [0] ⮌ Voltar")
    
    while True:
        try:
            escolha = int(input("\nQual ataque usar? ⯈ "))
            if escolha == 0:
                return None
            if 1 <= escolha <= len(personagem.ataques):
                return personagem.ataques[escolha - 1]
            print("❌ Opção inválida!")
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números.")


def menu_escolher_magia(personagem):
    """Exibe a lista de magias do personagem e verifica o custo de MP."""
    limpar_tela()
    exibir_cabecalho("ESCOLHER MAGIA")
    print(f"\nMagias de {personagem.nome} (MP Atual: {personagem.mp_atual}/{personagem.mp_max}):")
    
    for i, magia in enumerate(personagem.magias):
        print(f"[{i+1}] {magia.nome} (Poder: {magia.poder_base} | Custo MP: {magia.custo_mp})")
        print(f"     └ {magia.descricao}")
    print("\n [0] ⮌ Voltar")
    
    while True:
        try:
            escolha = int(input("\nQual magia conjurar? ⯈ "))
            if escolha == 0:
                return None
            if 1 <= escolha <= len(personagem.magias):
                magia_escolhida = personagem.magias[escolha - 1]
                if personagem.mp_atual < magia_escolhida.custo_mp:
                    print("❌ MP insuficiente para esta magia!")
                    continue
                return magia_escolhida
            print("❌ Opção inválida!")
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números.")


def menu_escolher_alvo(alvos):
    """
    Permite ao jogador escolher um alvo vivo.
    Aceita tanto a lista de 'inimigos' quanto a sua própria 'equipe'.
    """
    limpar_tela() 
    exibir_cabecalho("ESCOLHER ALVO")
    
    vivos = [alvo for alvo in alvos if alvo.esta_vivo()]
    
    for i, alvo in enumerate(vivos):
        print(f"[{i+1}] {alvo.nome} (HP: {alvo.hp_atual}/{alvo.hp_max})")
    print("\n[0] Cancelar")
    
    while True:
        try:
            escolha = int(input("\nQuem será o alvo? ⯈ "))
            if escolha == 0:
                return None
            if 1 <= escolha <= len(vivos):
                return vivos[escolha - 1]
            print("❌ Opção inválida!")
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números.")


def menu_usar_item(party, inventario_total):
    """
    Exibe os itens disponíveis no inventário coletivo da equipe.
    Permite escolher o item e, em seguida, o aliado alvo.
    
    Parâmetros:
        party: lista de todos os membros da equipe (para escolher alvo)
        inventario_total: lista de tuplas (dono, item) com todos os itens da equipe

    Retorna:
        (dono, item, alvo) se o jogador confirmar, ou None se cancelar.
    """
    limpar_tela()
    exibir_cabecalho("USAR ITEM")
    print(f"\n  Inventário da equipe:\n")

    for i, (dono, item) in enumerate(inventario_total):
        print(f"  [{i+1}] {item.nome}")
        print(f"       └ {item.descricao}  (de: {dono.nome})")
    print("\n  [0] ⮌ Voltar")

    while True:
        try:
            escolha = int(input("\n  Qual item usar? ⯈ "))
            if escolha == 0:
                return None
            if 1 <= escolha <= len(inventario_total):
                dono, item_escolhido = inventario_total[escolha - 1]
                break
            print("❌ Opção inválida!")
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números.")

    # Itens de cura/buff sempre miram em um aliado
    limpar_tela()
    exibir_cabecalho("ESCOLHER ALVO DO ITEM")
    print(f"\n  Usando: {item_escolhido.nome}")
    print(f"  Escolha um aliado:\n")

    vivos = [m for m in party if m.esta_vivo()]
    for i, membro in enumerate(vivos):
        print(f"  [{i+1}] {membro.nome} (HP: {membro.hp_atual}/{membro.hp_max} | MP: {membro.mp_atual}/{membro.mp_max})")
    print("\n  [0] ⮌ Cancelar")

    while True:
        try:
            escolha = int(input("\n  Quem receberá o item? ⯈ "))
            if escolha == 0:
                return None
            if 1 <= escolha <= len(vivos):
                return (dono, item_escolhido, vivos[escolha - 1])
            print("❌ Opção inválida!")
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números.")