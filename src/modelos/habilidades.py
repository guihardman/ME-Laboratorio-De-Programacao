"""
Módulo: habilidades.py
Descrição: Define as classes de Ataques e Magias, agora com suporte a 
efeitos secundários (como alterar defesa), e armazena o catálogo.
"""

class Ataque:
    """
    Representa um ataque físico.
    Pode conter efeitos secundários que afetam o alvo ou o usuário.
    """
    def __init__(self, nome, descricao, poder_base, chance_acerto=100, chance_critico=5, efeito_secundario=None, valor_efeito=0):
        self.nome = nome
        self.descricao = descricao
        self.poder_base = poder_base
        self.chance_acerto = chance_acerto
        self.chance_critico = chance_critico
        self.efeito_secundario = efeito_secundario
        self.valor_efeito = valor_efeito

class Magia:
    """
    Representa uma habilidade mágica.
    Pode conter efeitos secundários que afetam o alvo ou o usuário.
    """
    def __init__(self, nome, descricao, elemento, poder_base, custo_mp, efeito_secundario=None, valor_efeito=0):
        self.nome = nome
        self.descricao = descricao
        self.elemento = elemento.lower()
        self.poder_base = poder_base
        self.custo_mp = custo_mp
        self.efeito_secundario = efeito_secundario
        self.valor_efeito = valor_efeito


# ==========================================
# CATÁLOGO DE HABILIDADES (Banco de Dados)
# ==========================================

CATALOGO_ATAQUES = {
    "corte_basico": Ataque(
        nome="Corte Básico", 
        descricao="Um ataque simples com a arma.", 
        poder_base=20, 
        chance_acerto=95
    ),
    "ataque_pesado": Ataque(
        nome="Ataque Pesado", 
        descricao="Um golpe lento, mas com alta chance de dano crítico.", 
        poder_base=40, 
        chance_acerto=70, 
        chance_critico=10
    ),
    "quebra_escudos": Ataque(
        nome="Quebra-Escudos", 
        descricao="Um golpe focado em destruir a armadura inimiga. Reduz a Defesa do alvo em 5.", 
        poder_base=15, 
        chance_acerto=85,
        efeito_secundario="reduzir_defesa_alvo",
        valor_efeito=5
    )
}

CATALOGO_MAGIAS = {
    "bola_de_fogo": Magia(
        nome="Bola de Fogo", 
        descricao="Lança uma esfera incandescente. Causa dano extra em inimigos fracos contra fogo.", 
        elemento="fogo", 
        poder_base=45, 
        custo_mp=10
    ),
    "cura_basica": Magia(
        nome="Cura Básica", 
        descricao="Restaura uma quantidade moderada de HP de um aliado.", 
        elemento="cura", 
        poder_base=30, 
        custo_mp=15
    ),
    "pele_de_pedra": Magia(
        # NOVO: Magia focada apenas em buff (poder base 0)
        nome="Pele de Pedra", 
        descricao="Endurece a pele do alvo. Aumenta a Defesa em 10 para o resto da batalha.", 
        elemento="terra", 
        poder_base=0, 
        custo_mp=12,
        efeito_secundario="aumentar_defesa_alvo",
        valor_efeito=10
    )
}