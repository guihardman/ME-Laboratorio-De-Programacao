import time
import random

from modulos.entidades import criar_personagem
from modulos.motor import determinar_iniciativa, verificar_vencedor, executar_acao

def iniciar_jogo():
    print("=" * 40)
    print("⚔️ BEM-VINDO À ARENA RPG ⚔️")
    print("=" * 40)
    
    # 1. SETUP: Criando dicionário usando a função do módulo entidades.py
    jogador = criar_personagem(
        nome="Herói", hp_maximo=100, mp_maximo=30, 
        ataque=25, defesa=10, poder_magico=40, resistencia_magica=15, velocidade=15
    )
    
    inimigo = criar_personagem(
        nome="Goblin Maligno", hp_maximo=80, mp_maximo=10, 
        ataque=18, defesa=5, poder_magico=10, resistencia_magica=5, velocidade=12
    )

    # 2. INICIATIVA: Perguntando ao motor.py quem começa
    turno_atual = determinar_iniciativa(jogador['velocidade'], inimigo['velocidade'])
    
    if turno_atual == 'p':
        print(f"\n⚡ Você ({jogador['nome']}) é mais rápido e ataca primeiro!")
    else:
        print(f"\n⚠️ O {inimigo['nome']} foi mais rápido e te surpreendeu!")

    # 3. GAME LOOP
    while verificar_vencedor(jogador, inimigo) == "Andamento":
        print("-" * 40)
        # HUD
        print(f"[{jogador['nome']}] HP: {jogador['hp_atual']}/{jogador['hp_maximo']} | MP: {jogador['mp_atual']}/{jogador['mp_maximo']}")
        print(f"[{inimigo['nome']}] HP: {inimigo['hp_atual']}/{inimigo['hp_maximo']}")
        print("-" * 40)
        
        # TURNO DO JOGADOR
        if turno_atual == 'p':
            acao_escolhida = input("Sua vez! Escolha [atacar / curar / magia]: ").strip().lower()
            
            try:
                executar_acao(atacante=jogador, defensor=inimigo, tipo_acao=acao_escolhida)
                print(f"✅ Você executou a ação: {acao_escolhida}!")
                
                # Só passa o turno se a ação der certo
                turno_atual = 'inimigo' 
                
            except ValueError as erro:
  
                print(f"❌ Erro: {erro}")
                print("Tente novamente.")
                # Loop roda de novo e o jogador não perde a vez
                continue 
            
        # TURNO DO INIMIGO
        else:
            print(f"\nPassos pesados... É a vez do {inimigo['nome']}!")
            time.sleep(1.5) # Dá uma pausa dramática para o jogador conseguir ler
            
            # IA simples: o inimigo tem 80% de chance de atacar e 20% de tentar se curar
            acao_inimigo = random.choices(['atacar', 'curar'], weights=[80, 20])[0]
            
            try:
                executar_acao(atacante=inimigo, defensor=jogador, tipo_acao=acao_inimigo)
                print(f"💥 O {inimigo['nome']} decidiu {acao_inimigo}!")
            except ValueError:
                # Se o inimigo tentar curar com vida cheia e der erro, ele perde o turno (burrice da IA)
                pass
            
            # Devolve o turno pro jogador
            turno_atual = 'p'
            time.sleep(1)

    # 4. FIM DE JOGO
    vencedor_final = verificar_vencedor(jogador, inimigo)
    
    print("\n" + "=" * 40)
    if vencedor_final == "Jogador":
        print("🏆 VITÓRIA! Você derrotou o monstro!")
    elif vencedor_final == "Inimigo":
        print("💀 GAME OVER! Você foi derrotado...")
    else:
        print("🤝 EMPATE! Ambos caíram no campo de batalha.")


if __name__ == "__main__":
    iniciar_jogo()