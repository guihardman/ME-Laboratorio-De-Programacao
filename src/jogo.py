"""
Módulo: jogo.py
Descrição: Ponto de entrada principal do jogo. Agora com um sistema
dinâmico de seleção de personagens no início da partida e interface polida.
"""

import time
import random
import copy

from src.modelos.entidades import CATALOGO_PERSONAGENS, CATALOGO_INIMIGOS
from src.sistemas.mapa import Mapa
from src.sistemas.combate import iniciar_combate
from src.utils.interface import limpar_tela, exibir_cabecalho

def preparar_equipe_inicial():
    """
    Exibe um menu iterativo para o jogador montar sua party de 3 membros
    escolhendo entre as classes disponíveis no catálogo.
    """
    party = []
    chaves_classes = list(CATALOGO_PERSONAGENS.keys())
    
    for i in range(3):
        limpar_tela() # Limpa o ecrã a cada nova escolha
        exibir_cabecalho("MONTAGEM DA EQUIPE")
        print("\n 👑 O Rei convocou 3 heróis para limpar a Floresta do Início.\n")
        
        # Mostra quem já está na equipa para o jogador não se perder
        if party:
            print(" 🛡️  Equipa Atual:")
            for membro in party:
                print(f"    - {membro.nome}")
            print() # Espaço extra para separar do menu
            
        print(f" ┌── Escolhendo o {i+1}º membro da Party ──┐")
        
        # Lista as opções disponíveis exibindo NOME e DESCRIÇÃO
        for j, chave in enumerate(chaves_classes):
            modelo = CATALOGO_PERSONAGENS[chave]
            print(f" │ [{j+1}] {modelo.nome}")
            print(f" │     └ {modelo.descricao}")
        print(" └" + "─" * 37 + "┘")
        
        while True:
            try:
                escolha = int(input("\n ⯈ Escolha a classe (1-4): "))
                if 1 <= escolha <= len(chaves_classes):
                    chave_escolhida = chaves_classes[escolha - 1]
                    
                    # Cria uma CÓPIA INDEPENDENTE do modelo para a party
                    heroi_escolhido = copy.deepcopy(CATALOGO_PERSONAGENS[chave_escolhida])
                    party.append(heroi_escolhido)
                    
                    print(f" ✔️  {heroi_escolhido.nome} juntou-se à equipa!\n")
                    time.sleep(1)
                    break # Sai do while e vai para o próximo membro
                else:
                    print(" ❌ Opção inválida! Escolha um número da lista.")
            except ValueError:
                print(" ❌ Digite um número válido!")
                
    return party

def gerar_inimigos_aleatorios():
    """
    Sorteia de 1 a 3 inimigos do catálogo para formar o grupo adversário.
    """
    quantidade = random.randint(1, 3)
    grupo = []
    chaves_inimigos = list(CATALOGO_INIMIGOS.keys())
    
    for _ in range(quantidade):
        chave_sorteada = random.choice(chaves_inimigos)
        monstro = copy.deepcopy(CATALOGO_INIMIGOS[chave_sorteada])
        grupo.append(monstro)
        
    return grupo

def main():
    """Loop principal do jogo."""
    limpar_tela()
    exibir_cabecalho("RPG: O DESPERTAR DO PYTHON")
    time.sleep(1.5)
    
    # Chama a função interativa de montagem
    party = preparar_equipe_inicial()
    
    limpar_tela()
    exibir_cabecalho("INÍCIO DA JORNADA")
    print("\n 🌲 A equipa entra na floresta escura. Fiquem atentos...\n")
    time.sleep(2)
    
    mapa = Mapa()
    jogando = True

    while jogando:
        mapa.desenhar()
        acao = input("\n ⯈ Comandos [W, A, S, D] | Ação: ").lower()
        
        evento = mapa.mover_jogador(acao)

        if evento == "EVENTO_BATALHA":
            limpar_tela()
            exibir_cabecalho("ENCONTRO ALEATÓRIO")
            print("\n ⚔️  Inimigos saltaram das sombras!")
            time.sleep(1)
            
            inimigos = gerar_inimigos_aleatorios()
            vitoria = iniciar_combate(party, inimigos)
            
            if not vitoria:
                limpar_tela()
                exibir_cabecalho("GAME OVER")
                print("\n 🪦 A sua jornada terminou nas cinzas...")
                jogando = False
                
        elif evento == "EVENTO_BAU":
            print("\n 🎁 Encontrou um baú escondido nas folhagens!")
            time.sleep(2)
            
        elif evento == "EVENTO_SAIDA":
            limpar_tela()
            exibir_cabecalho("VITÓRIA")
            print("\n 🎉 A equipa conseguiu atravessar a Floresta do Início em segurança!")
            print(" Obrigado por jogar!\n")
            jogando = False