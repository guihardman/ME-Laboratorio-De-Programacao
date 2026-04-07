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
        self.defesa_base = defesa
        self.defesa_atual = defesa
        self.agilidade = agilidade
        
        self.ataques = []
        self.magias = []

    def esta_vivo(self):
        """Verifica se a entidade ainda tem pontos de vida."""
        return self.hp_atual > 0

    def receber_dano(self, dano):
        """Reduz o HP da entidade. O max() garante que o HP nunca fique negativo."""
        self.hp_atual = max(0, self.hp_atual - dano)

    def gastar_mp(self, custo):
        """Tenta gastar MP. Retorna True se tiver sucesso, False se não tiver MP suficiente."""
        if self.mp_atual >= custo:
            self.mp_atual -= custo
            return True
        return False

    def acao_defender(self):
        """Dobra a defesa atual exclusivamente para o turno vigente."""
        self.defesa_atual = self.defesa_base * 2

    def resetar_defesa(self):
        """Restaura a defesa para o valor base no início de um novo turno."""
        self.defesa_atual = self.defesa_base


class Personagem(Entidade):
    """
    Classe para os heróis controlados pelo jogador. Herda da superclasse Entidade.
    """
    def __init__(self, nome, hp_max, mp_max, forca, inteligencia, defesa, agilidade):
        super().__init__(nome, hp_max, mp_max, forca, inteligencia, defesa, agilidade)
        self.inventario = [] 
        self.descricao = "" # Atributo para exibir o texto de lore/história no menu de seleção


class Inimigo(Entidade):
    """
    Classe para os monstros controlados pela IA. Herda da superclasse Entidade.
    """
    def __init__(self, nome, hp_max, mp_max, forca, inteligencia, defesa, agilidade, fraqueza_elemento=None):
        super().__init__(nome, hp_max, mp_max, forca, inteligencia, defesa, agilidade)
        self.fraqueza = fraqueza_elemento


# ==========================================
#               CATÁLOGOS
# ==========================================

# 1. HERÓIS
guerreiro = Personagem("Prof. Fernando (Guerreiro)", hp_max=100, mp_max=30, forca=18, inteligencia=5, defesa=8, agilidade=10)
guerreiro.descricao = "O maioral, o héroi de todos nós. Possui muita vida e defesa."
guerreiro.ataques.append(CATALOGO_ATAQUES["corte_basico"])
guerreiro.ataques.append(CATALOGO_ATAQUES["ataque_pesado"])
guerreiro.ataques.append(CATALOGO_ATAQUES["quebra_escudos"])

mago = Personagem("Edra (Mago)", hp_max=60, mp_max=80, forca=5, inteligencia=20, defesa=4, agilidade=12)
mago.descricao = "Mestre das ias. Causa dano mágico massivo, mas é muito frágil."
mago.ataques.append(CATALOGO_ATAQUES["corte_basico"])
mago.magias.append(CATALOGO_MAGIAS["bola_de_fogo"])
mago.magias.append(CATALOGO_MAGIAS["raio_de_gelo"])
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
ladino.ataques.append(CATALOGO_ATAQUES["mordida_desdentada"])

CATALOGO_PERSONAGENS = {
    "guerreiro": guerreiro,
    "mago": mago,
    "clerigo": clerigo,
    "ladino": ladino
}

# 2. INIMIGOS
lafeu = Inimigo("Lafeu papai", hp_max=40, mp_max=0, forca=12, inteligencia=2, defesa=2, agilidade=15, fraqueza_elemento="gelo")
lafeu.ataques.append(CATALOGO_ATAQUES["corte_basico"])

porca = Inimigo("Porca do Lauro", hp_max=80, mp_max=0, forca=20, inteligencia=2, defesa=6, agilidade=5, fraqueza_elemento="fogo")
porca.ataques.append(CATALOGO_ATAQUES["ataque_pesado"])

irmaos = Inimigo("Tropa dos IRMAOS", hp_max=30, mp_max=0, forca=14, inteligencia=1, defesa=3, agilidade=20, fraqueza_elemento="fogo")
irmaos.ataques.append(CATALOGO_ATAQUES["corte_basico"])

CATALOGO_INIMIGOS = {
    "lafeu": lafeu,
    "porca_do_lauro": porca,
    "tropa_dos_irmaos": irmaos
}
