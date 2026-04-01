"""
Módulo: entidades.py
Descrição: Define as classes base (Herança) para os seres vivos do jogo e 
armazena os catálogos (banco de dados em memória) de Heróis e Inimigos.
"""

from .habilidades import CATALOGO_ATAQUES, CATALOGO_MAGIAS

class Entidade:
    """
    Superclasse que contém as regras fundamentais de qualquer ser no jogo.
    """
    def __init__(self, nome, hp_max, mp_max, forca, inteligencia, defesa, agilidade):
        self.nome = nome
        self.hp_max = hp_max
        self.hp_atual = hp_max
        self.mp_max = mp_max
        self.mp_atual = mp_max
        self.forca = forca
        self.inteligencia = inteligencia
        
        # O sistema de defesa dupla para gerenciar buffs temporários
        self.defesa_base = defesa
        self.defesa_atual = defesa
        self.agilidade = agilidade
        
        self.ataques = []
        self.magias = []

    def esta_vivo(self):
        return self.hp_atual > 0

    def receber_dano(self, dano):
        # max() garante que o HP nunca fique negativo (menor que zero)
        self.hp_atual = max(0, self.hp_atual - dano)

    def gastar_mp(self, custo):
        if self.mp_atual >= custo:
            self.mp_atual -= custo
            return True
        return False

    def acao_defender(self):
        # Dobra a defesa atual para o turno
        self.defesa_atual = self.defesa_base * 2

    def resetar_defesa(self):
        # Restaura a defesa para o valor base
        self.defesa_atual = self.defesa_base


class Personagem(Entidade):
    """
    Classe para os heróis controlados pelo jogador. Herda de Entidade.
    """
    def __init__(self, nome, hp_max, mp_max, forca, inteligencia, defesa, agilidade):
        super().__init__(nome, hp_max, mp_max, forca, inteligencia, defesa, agilidade)
        self.inventario = [] 
        self.descricao = "" # Atributo adicionado para exibir no menu


class Inimigo(Entidade):
    """
    Classe para os monstros controlados pela IA. Herda de Entidade.
    """
    def __init__(self, nome, hp_max, mp_max, forca, inteligencia, defesa, agilidade, fraqueza_elemento=None):
        super().__init__(nome, hp_max, mp_max, forca, inteligencia, defesa, agilidade)
        self.fraqueza = fraqueza_elemento


# ==========================================
# CATÁLOGOS (O "Banco de Dados" do Jogo)
# ==========================================

# 1. MONTANDO OS HERÓIS (Modelos para a Party)
guerreiro = Personagem("Porca (Guerreiro)", hp_max=100, mp_max=30, forca=18, inteligencia=5, defesa=8, agilidade=10)
guerreiro.descricao = "Usa o próprio peso para potencializar seus golpes. Possui muita vida e defesa."
guerreiro.ataques.append(CATALOGO_ATAQUES["corte_basico"])
guerreiro.ataques.append(CATALOGO_ATAQUES["ataque_pesado"])
guerreiro.ataques.append(CATALOGO_ATAQUES["quebra_escudos"])

mago = Personagem("Edra (Mago)", hp_max=60, mp_max=80, forca=5, inteligencia=20, defesa=4, agilidade=12)
mago.descricao = "Mestre das ias. Causa dano mágico massivo, mas é muito frágil."
mago.ataques.append(CATALOGO_ATAQUES["corte_basico"])
mago.magias.append(CATALOGO_MAGIAS["bola_de_fogo"])
mago.magias.append(CATALOGO_MAGIAS["pele_de_pedra"])

clerigo = Personagem("Seu Nabih (Clérigo)", hp_max=80, mp_max=60, forca=10, inteligencia=15, defesa=6, agilidade=11)
clerigo.descricao = "Apoio vital para a equipe. Capaz de curar aliados e fortalecer defesas."
clerigo.ataques.append(CATALOGO_ATAQUES["corte_basico"])
clerigo.magias.append(CATALOGO_MAGIAS["cura_basica"])
clerigo.magias.append(CATALOGO_MAGIAS["pele_de_pedra"])

ladino = Personagem("Dentes (Ladino)", hp_max=75, mp_max=40, forca=14, inteligencia=8, defesa=5, agilidade=18)
ladino.descricao = "Ataca com os poucos dentes que tem. Ataca rápido e tem alta chance de acertos críticos."
ladino.ataques.append(CATALOGO_ATAQUES["corte_basico"])
ladino.ataques.append(CATALOGO_ATAQUES["ataque_pesado"])

CATALOGO_PERSONAGENS = {
    "guerreiro": guerreiro,
    "mago": mago,
    "clerigo": clerigo,
    "ladino": ladino
}

# 2. MONTANDO OS INIMIGOS (Modelos para os Encontros)
goblin = Inimigo("Goblin", hp_max=40, mp_max=0, forca=12, inteligencia=2, defesa=2, agilidade=15, fraqueza_elemento="fogo")
goblin.ataques.append(CATALOGO_ATAQUES["corte_basico"])

orc = Inimigo("Orc Brutal", hp_max=80, mp_max=0, forca=20, inteligencia=2, defesa=6, agilidade=5, fraqueza_elemento="terra")
orc.ataques.append(CATALOGO_ATAQUES["ataque_pesado"])

lobo = Inimigo("Lobo Selvagem", hp_max=30, mp_max=0, forca=14, inteligencia=1, defesa=3, agilidade=20, fraqueza_elemento="fogo")
lobo.ataques.append(CATALOGO_ATAQUES["corte_basico"])

CATALOGO_INIMIGOS = {
    "goblin": goblin,
    "orc_brutal": orc,
    "lobo_selvagem": lobo
}