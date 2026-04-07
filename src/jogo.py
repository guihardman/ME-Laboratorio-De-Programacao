import time
import random
import copy

from src.modelos.entidades import CATALOGO_PERSONAGENS, CATALOGO_INIMIGOS
from src.modelos.itens import CATALOGO_ITENS
from src.sistemas.mapa import Mapa
from src.sistemas.combate import iniciar_combate
from src.utils.interface import limpar_tela, exibir_cabecalho

def gerar_inimigos_aleatorios():
    """
    Gera um grupo de 1 a 3 inimigos aleatórios copiados do catálogo
    para que cada batalha seja independente.
    """
    inimigos = []
    chaves_inimigos = list(CATALOGO_INIMIGOS.keys())
    
    for _ in range(random.randint(1, 3)):
        chave_aleatoria = random.choice(chaves_inimigos)
        novo_inimigo = copy.deepcopy(CATALOGO_INIMIGOS[chave_aleatoria])
        inimigos.append(novo_inimigo)
        
    return inimigos

def abrir_bau(party):
    """
    Sorteia um item do catálogo, exibe uma mensagem e o adiciona ao
    inventário de um membro aleatório da party que ainda esteja vivo.
    """
    chaves_itens = list(CATALOGO_ITENS.keys())
    chave_sorteada = random.choice(chaves_itens)
    item_encontrado = copy.deepcopy(CATALOGO_ITENS[chave_sorteada])

    # Escolhe um portador vivo aleatório
    membros_vivos = [m for m in party if m.esta_vivo()]
    portador = random.choice(membros_vivos) if membros_vivos else party[0]
    portador.inventario.append(item_encontrado)

    limpar_tela()
    exibir_cabecalho("BAÚ ENCONTRADO!")
    print(f"\n  🎁 A equipe abriu um baú escondido nas folhagens!")
    print(f"\n  ✨ Item encontrado: {item_encontrado.nome}")
    print(f"     └ {item_encontrado.descricao}")
    print(f"\n  📦 {portador.nome} guardou o item no inventário.")
    print("\n  Inventário atual da equipe:")
    for membro in party:
        if membro.inventario:
            for item in membro.inventario:
                print(f"    - [{membro.nome}] {item.nome}")
    input("\n  Pressione ENTER para continuar...")

def preparar_equipe_inicial():
    """
    Exibe um menu iterativo para o jogador montar sua equipe de 3 membros
    escolhendo entre as classes disponíveis no catálogo.
    """
    party = []
    chaves_classes = list(CATALOGO_PERSONAGENS.keys())
    
    for i in range(3):
        escolha_valida = False
        while not escolha_valida:
            limpar_tela()
            exibir_cabecalho("MONTAGEM DA EQUIPE")
            print("\n 👑 O Rei convocou 3 heróis para limpar a Floresta do Início.\n")
            
            if party:
                print(" 🛡️  Equipe Atual:")
                for membro in party:
                    print(f"    - {membro.nome}")
                print() 
                
            print(f" ┌── Escolhendo o {i+1}º membro da equipe ──┐")
            
            for j, chave in enumerate(chaves_classes):
                personagem = CATALOGO_PERSONAGENS[chave]
                print(f" [{j+1}] {personagem.nome}")
                print(f"     └ {personagem.descricao}\n")
                
            try:
                escolha = int(input(f"Escolha a classe para o {i+1}º herói: "))
                
                if 1 <= escolha <= len(chaves_classes):
                    chave_escolhida = chaves_classes[escolha - 1]
                    novo_membro = copy.deepcopy(CATALOGO_PERSONAGENS[chave_escolhida])
                    party.append(novo_membro)
                    escolha_valida = True
                else:
                    print("\n❌ Opção inválida! Escolha um número da lista.")
                    time.sleep(1.5)
            except ValueError:
                print("\n❌ Entrada inválida! Por favor, digite apenas números.")
                time.sleep(1.5)
                
    return party

def main():
    """Função principal que gerencia o fluxo de exploração do mapa."""
    limpar_tela()
    exibir_cabecalho("RPG: O DESPERTAR DA PORCA")
    time.sleep(1.5)
    
    party = preparar_equipe_inicial()
    
    limpar_tela()
    exibir_cabecalho("INÍCIO DA JORNADA")
    print("\n 🌲 A equipe entra na floresta escura. Fiquem atentos...\n")
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
            abrir_bau(party)
            
        elif evento == "EVENTO_SAIDA":
            limpar_tela()
            exibir_cabecalho("VITÓRIA!")
            print("\n 🎉 A equipe encontrou a saída da floresta em segurança!")
            print(" FIM DA DEMONSTRAÇÃO. Nota 10, professor! ;)\n")
            jogando = False