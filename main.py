import time
import random
import os

from modulos.entidades import criar_personagem
from modulos.motor import determinar_iniciativa, verificar_vencedor, executar_acao

def limpar_tela():
    """Limpa o terminal para dar sensação de tela fixa (HUD)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def criar_barra(valor_atual: int, valor_maximo: int, tamanho: int = 15) -> str:
    """Cria uma barra de progresso visual simples."""
    if valor_maximo <= 0:
        return f"[{'░' * tamanho}]"
        
    porcentagem = valor_atual / valor_maximo
    blocos_cheios = int(tamanho * porcentagem)
    
    # Garante que não vai bugar se a porcentagem passar de 100 ou cair abaixo de 0
    blocos_cheios = min(max(blocos_cheios, 0), tamanho)
    blocos_vazios = tamanho - blocos_cheios
    
    return f"[{'█' * blocos_cheios}{'░' * blocos_vazios}]"

def iniciar_jogo():
    limpar_tela()
    print("=" * 45)
    print(" ⚔️  BEM-VINDO À ARENA RPG  ⚔️ ".center(45))
    print("=" * 45 + "\n")
    
    # CRIAÇÃO DE PERSONAGEM
    nome_jogador = input("✍️  Digite o nome do seu herói: ")
    print("\n🛡️  ESCOLHA SUA CLASSE:")
    print("  [1] Guerreiro  (Alto HP, Alto Dano)")
    print("  [2] Mago       (Baixo HP, Alta Magia)")
    print("  [3] Paladino   (Equilibrado, Cura)")
    
    escolha = input("\n➤ Qual a sua classe? (Guerreiro, Mago, Paladino): ")
    
    try:
        jogador = criar_personagem(nome=nome_jogador, classe_escolhida=escolha)
    except ValueError:
        print("\n⚠️  Opção inválida! Você será um Guerreiro por padrão.")
        jogador = criar_personagem(nome=nome_jogador, classe_escolhida="guerreiro")
        time.sleep(2)
        
    # Criando o boss
    inimigo = criar_personagem(nome="Porca do Lauro", classe_escolhida="guerreiro")
    inimigo['hp_maximo'] = 150 
    inimigo['hp_atual'] = 150

    limpar_tela()
    print(f"🔥 O grande portão se abre... {inimigo['nome']} aparece! 🔥\n")
    time.sleep(2)

    # Determinando quem começa
    turno_atual = determinar_iniciativa(jogador['velocidade'], inimigo['velocidade'])
    
    if turno_atual == 'p':
        print(f"⚡ Você ({jogador['classe']}) é mais rápido e ataca primeiro!")
    else:
        print(f"⚠️  O {inimigo['nome']} te pegou de surpresa!")
    time.sleep(2)

    # GAME LOOP
    while verificar_vencedor(jogador, inimigo) == "Andamento":
        limpar_tela()
        
        # HUD (Interface de Status)
        print("=" * 45)
        print(f"🧑 {jogador['nome'].upper()} ({jogador['classe']})")
        print(f"❤️  HP: {criar_barra(jogador['hp_atual'], jogador['hp_maximo'])} {jogador['hp_atual']:>3}/{jogador['hp_maximo']}")
        print(f"✨ MP: {criar_barra(jogador['mp_atual'], jogador['mp_maximo'], 10)} {jogador['mp_atual']:>3}/{jogador['mp_maximo']}")
        print("-" * 45)
        print(f"👹 {inimigo['nome'].upper()}")
        print(f"❤️  HP: {criar_barra(inimigo['hp_atual'], inimigo['hp_maximo'])} {inimigo['hp_atual']:>3}/{inimigo['hp_maximo']}")
        print("=" * 45 + "\n")
        
        # TURNO DO JOGADOR
        if turno_atual == 'p':
            print("Sua vez! O que você faz?")
            print("  [A]tacar   [C]urar   [M]agia")
            acao_input = input("➤ ").strip().lower()
            
            # Atalhos amigáveis
            if acao_input in ['a', 'atacar']: acao_escolhida = 'atacar'
            elif acao_input in ['c', 'curar']: acao_escolhida = 'curar'
            elif acao_input in ['m', 'magia']: acao_escolhida = 'magia'
            else: acao_escolhida = acao_input # Cai no erro do motor se for nada a ver
            
            nome_feitico = ""
            
            if acao_escolhida == 'magia':
                print(f"\n🔮 Suas magias: {', '.join(jogador['magias']).title()}")
                nome_feitico = input("Qual magia usar? (ou digite 'voltar'): ").strip().lower()
                
                if nome_feitico == 'voltar':
                    continue # Volta para o começo do loop
            
            try:
                executar_acao(atacante=jogador, defensor=inimigo, tipo_acao=acao_escolhida, nome_magia=nome_feitico)
                print(f"\n✅ Ação '{acao_escolhida}' executada com sucesso!")
                turno_atual = 'inimigo' 
            except ValueError as erro:
                print(f"\n❌ Erro: {erro}")
                time.sleep(2)
                continue 
            
            time.sleep(2)
            
        # TURNO DO INIMIGO
        else:
            print(f"O {inimigo['nome']} está se preparando...")
            time.sleep(1.5) 
            
            acao_inimigo = random.choices(['atacar', 'curar'], weights=[80, 20])[0]
            
            try:
                executar_acao(atacante=inimigo, defensor=jogador, tipo_acao=acao_inimigo)
                print(f"\n💥 O inimigo usou: {acao_inimigo.upper()}!")
            except ValueError:
                pass
            
            turno_atual = 'p'
            time.sleep(2)

    # FIM DE JOGO
    limpar_tela()
    vencedor_final = verificar_vencedor(jogador, inimigo)
    
    print("=" * 45)
    if vencedor_final == "Jogador":
        print("🏆 VITÓRIA ÉPICA!".center(45))
        print(f"O {inimigo['nome']} caiu perante a sua força!".center(45))
    elif vencedor_final == "Inimigo":
        print("💀 GAME OVER...".center(45))
        print("O mundo mergulhou nas trevas.".center(45))
    else:
        print("🤝 EMPATE! Ambos caíram em combate.".center(45))
    print("=" * 45 + "\n")

if __name__ == "__main__":
    iniciar_jogo()