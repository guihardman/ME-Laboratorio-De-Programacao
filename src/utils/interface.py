"""
Módulo: interface.py
Descrição: Gerencia todos os menus e a exibição de informações no terminal.
Isola a interação com o usuário (prints e inputs) da lógica de combate.
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
    
    # --- Painel da Party ---
    print(" 🛡️  SUA EQUIPE:")
    for p in party:
        if p.esta_vivo():
            barra_hp = f"HP: {p.hp_atual: >3}/{p.hp_max: <3}"
            barra_mp = f"MP: {p.mp_atual: >2}/{p.mp_max: <2}"
            print(f"  ⯈ {p.nome: <20} │ {barra_hp} │ {barra_mp}")
        else:
            print(f"  ⯈ {p.nome: <20} │ [ ☠️ CAÍDO ]")
            
    print("─" * tamanho)
    
    # --- Painel dos Inimigos ---
    print(" 💀 INIMIGOS:")
    for i, inimigo in enumerate(inimigos):
        if inimigo.esta_vivo():
            barra_hp = f"HP: {inimigo.hp_atual: >3}/{inimigo.hp_max: <3}"
            print(f"  [{i+1}] {inimigo.nome: <18} │ {barra_hp}")
        else:
            print(f"  [{i+1}] {inimigo.nome: <18} │ [ ☠️ DERROTADO ]")
            
    print("=" * tamanho + "\n")

def menu_escolher_acao(personagem):
    """Exibe o menu principal de turno para um personagem."""
    tamanho = 56
    print("┌" + "─" * (tamanho - 2) + "┐")
    print(f"│ O que {personagem.nome} vai fazer?".ljust(tamanho - 1) + "│")
    print("├" + "─" * (tamanho - 2) + "┤")
    print("│ [1] ⚔️ Atacar                         [3] 🛡️ Defender  │")
    print("│ [2] ✨ Magia                         [4] 🎒 Item     │")
    print("└" + "─" * (tamanho - 2) + "┘")
    
    while True:
        escolha = input("Ação ⯈ ")
        if escolha in ['1', '2', '3', '4']:
            return int(escolha)
        print("Opção inválida! Escolha 1, 2, 3 ou 4.")

def menu_escolher_ataque(personagem):
    """Mostra os ataques físicos disponíveis."""
    exibir_cabecalho(f"ATAQUES: {personagem.nome}")
    
    for i, ataque in enumerate(personagem.ataques):
        print(f" [{i+1}] {ataque.nome} (Poder: {ataque.poder_base})")
        print(f"     └ {ataque.descricao}")
    print("\n [0] ⮌ Voltar")
    
    while True:
        try:
            escolha = int(input("\nQual ataque usar? ⯈ "))
            if escolha == 0:
                return None
            if 1 <= escolha <= len(personagem.ataques):
                return personagem.ataques[escolha - 1]
            print("Opção inválida!")
        except ValueError:
            print("Digite um número válido!")

def menu_escolher_magia(personagem):
    """Mostra as magias disponíveis e o custo de MP."""
    exibir_cabecalho(f"MAGIAS: {personagem.nome}")
    
    if not personagem.magias:
        print("  Este personagem não possui magias.")
        print("\n [0] ⮌ Voltar")
        while True:
            if input("⯈ ") == '0': return None
            
    for i, magia in enumerate(personagem.magias):
        mp_status = f"Custo: {magia.custo_mp} MP"
        if personagem.mp_atual < magia.custo_mp:
            mp_status = f"INSUFICIENTE (Custa {magia.custo_mp})"
        print(f" [{i+1}] {magia.nome} ({mp_status})")
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
            print("Opção inválida!")
        except ValueError:
            print("Digite um número válido!")

def menu_escolher_alvo(inimigos):
    """Permite ao jogador escolher qual inimigo vivo atacar."""
    limpar_tela() # <--- Adicionámos a limpeza de ecrã aqui!
    exibir_cabecalho("ESCOLHER ALVO")
    
    # Cria uma lista apenas com os inimigos vivos para evitar bater em cadáveres
    vivos = [inimigo for inimigo in inimigos if inimigo.esta_vivo()]
    
    for i, inimigo in enumerate(vivos):
        print(f"[{i+1}] {inimigo.nome} (HP: {inimigo.hp_atual}/{inimigo.hp_max})")
    print("[0] Cancelar")
    
    while True:
        try:
            escolha = int(input("\nQuem será o alvo? "))
            if escolha == 0:
                return None
            if 1 <= escolha <= len(vivos):
                return vivos[escolha - 1]
            print("Opção inválida!")
        except ValueError:
            print("Digite um número válido!")