"""
Módulo: mapa.py
Descrição: Gerencia a grade do cenário, a posição do jogador e os encontros aleatórios.
"""

import random
from src.utils.interface import limpar_tela, exibir_cabecalho

class Mapa:
    def __init__(self):
        # A grade do mapa (Matriz 2D)
        # '#' = Parede / Árvore (Bloqueia movimento)
        # '.' = Chão livre (Pode ter batalha aleatória)
        # 'B' = Baú de Item
        # 'S' = Saída ou Boss
        self.grade = [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', '.', '.', '.', 'B', '#', '.', '.', '.', '#'],
            ['#', '.', '#', '#', '.', '#', '.', '#', '.', '#'],
            ['#', '.', '.', '#', '.', '.', '.', '#', '.', '#'],
            ['#', '#', '.', '#', '#', '#', '.', '#', 'C', '#'],
            ['#', 'B', '.', '.', '.', '.', '.', '#', 'S', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
        ]
        
        # Posição inicial do jogador (linha, coluna) -> (y, x)
        self.jogador_y = 1
        self.jogador_x = 1

    def desenhar(self):
        """Limpa a tela e imprime o mapa atualizado com moldura e legenda."""
        limpar_tela()
        exibir_cabecalho("FLORESTA DO INÍCIO")

        largura_mapa = len(self.grade[0])
        
        # Topo da moldura do mapa (espaçamento duplo para ficar um quadrado mais bonito)
        print("\n    ┌" + "──" * largura_mapa + "─┐")

        # Percorre as linhas (y) e colunas (x) para desenhar a grade
        for y in range(len(self.grade)):
            linha_visual = "    │ "
            for x in range(len(self.grade[y])):
                # Se a coordenada atual for a mesma do jogador, desenha o 'P'
                if y == self.jogador_y and x == self.jogador_x:
                    linha_visual += "P "
                else:
                    # Desenha o caractere original do mapa
                    linha_visual += self.grade[y][x] + " "
            
            linha_visual += "│"
            print(linha_visual)
            
        # Fundo da moldura do mapa
        print("    └" + "──" * largura_mapa + "─┘")
        
        # Legenda Organizada
        print("\n  ┌── LEGENDA " + "─" * 40 + "┐")
        print("  │  [P] Herói    [#] Parede/Árvore    [.] Caminho    │")
        print("  │  [B] Baú      [S] Saída do Nível   [C] Chefe      │")
        print("  └" + "─" * 51 + "┘")

    def mover_jogador(self, direcao):
        """
        Recebe o input do jogador e tenta mover as coordenadas X e Y.
        Retorna uma string indicando o que aconteceu após o movimento.
        """
        # Variáveis temporárias para testar o próximo passo
        novo_y = self.jogador_y
        novo_x = self.jogador_x

        # Atualiza a coordenada temporária dependendo da tecla
        direcao = direcao.lower()
        if direcao == 'w': novo_y -= 1
        elif direcao == 's': novo_y += 1
        elif direcao == 'a': novo_x -= 1
        elif direcao == 'd': novo_x += 1
        else:
            return "INVALIDO"

        # Proteção extra: Checa se saiu dos limites da matriz
        if novo_y < 0 or novo_y >= len(self.grade) or novo_x < 0 or novo_x >= len(self.grade[0]):
            return "BLOQUEADO"

        # Checa colisão com parede usando a matriz original (não a visual)
        celula_destino = self.grade[novo_y][novo_x]
        if celula_destino == '#':
            return "BLOQUEADO"

        # Se chegou até aqui, o caminho está livre! Atualiza a posição do jogador.
        self.jogador_y = novo_y
        self.jogador_x = novo_x

        # ==========================================
        # ANÁLISE DO EVENTO DA CÉLULA (O Retorno)
        # ==========================================
        if celula_destino == 'B':
            # Remove o baú do mapa para não ser pego duas vezes
            self.grade[novo_y][novo_x] = '.' 
            return "EVENTO_BAU"
            
        elif celula_destino == 'S':
            return "EVENTO_SAIDA"
            
        elif celula_destino == '.':
            # Mecânica de "Dado Invisível" para encontros aleatórios
            chance_batalha = 15 # 15% de chance
            if random.randint(1, 100) <= chance_batalha:
                return "EVENTO_BATALHA"
                
        return "LIVRE"