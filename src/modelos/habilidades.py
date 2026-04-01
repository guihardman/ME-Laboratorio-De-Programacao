"""
Módulo: habilidades.py
Descrição: Define as classes de Ataques e Magias e armazena o catálogo 
de todas as habilidades disponíveis no jogo.
"""

class Ataque:
    """
    Representa um ataque físico.
    Usa a Força do atacante contra a Defesa do alvo.
    """
    def __init__(self, nome, poder_base, chance_acerto=100, chance_critico=5):
        self.nome = nome
        self.poder_base = poder_base
        self.chance_acerto = chance_acerto
        
        # A chance de crítico tem um valor padrão de 5%, mas pode ser 
        # sobrescrita se um ataque específico for mais letal.
        self.chance_critico = chance_critico

class Magia:
    """
    Representa uma habilidade mágica.
    Usa a Inteligência do atacante contra a Defesa do alvo.
    """
    def __init__(self, nome, elemento, poder_base, custo_mp):
        self.nome = nome
        self.elemento = elemento.lower()  # Padroniza para minúsculo para evitar bugs na comparação
        self.poder_base = poder_base
        self.custo_mp = custo_mp


# ==========================================
# CATÁLOGO DE HABILIDADES (Banco de Dados)
# ==========================================
# Usar dicionários aqui é uma excelente prática. Isso centraliza o balanceamento do jogo.
# Se acharem que a Bola de Fogo está forte demais, vocês alteram apenas nesta linha.

CATALOGO_ATAQUES = {
    "corte_basico": Ataque("Corte Básico", poder_base=20, chance_acerto=95),
    "ataque_pesado": Ataque("Ataque Pesado", poder_base=40, chance_acerto=70, chance_critico=10), # Menos chance de acerto, mais crítico
    "golpe_rapido": Ataque("Golpe Rápido", poder_base=15, chance_acerto=100, chance_critico=15),
    "esmagar": Ataque("Esmagar", poder_base=35, chance_acerto=80)
}

CATALOGO_MAGIAS = {
    "bola_de_fogo": Magia("Bola de Fogo", elemento="fogo", poder_base=45, custo_mp=10),
    "raio_de_gelo": Magia("Raio de Gelo", elemento="gelo", poder_base=40, custo_mp=8),
    "choque_eletrico": Magia("Choque Elétrico", elemento="raio", poder_base=50, custo_mp=12),
    
    # Magia especial que foge à regra de dano. Pode ser tratada de forma diferente no combate.py
    "cura_basica": Magia("Cura Básica", elemento="cura", poder_base=30, custo_mp=15) 
}