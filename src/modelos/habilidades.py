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
    Pode conter efeitos secundários que afetam o alvo e definir se deve mirar em aliados.
    """
    # NOVO: Adicionamos o parâmetro alvo_aliado (padrão é False para magias de dano)
    def __init__(self, nome, descricao, elemento, custo_mp, poder_base, chance_acerto=100, efeito_secundario=None, valor_efeito=0, alvo_aliado=False):
        self.nome = nome
        self.descricao = descricao
        self.elemento = elemento.lower()
        self.poder_base = poder_base
        self.chance_acerto = chance_acerto
        self.custo_mp = custo_mp
        self.efeito_secundario = efeito_secundario
        self.valor_efeito = valor_efeito
        self.alvo_aliado = alvo_aliado


# ==========================================
#          CATÁLOGO DE HABILIDADES
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
        descricao="Um golpe focado em destruir a armadura inimiga. Reduz a Defesa do alvo em 10.", 
        poder_base=30, 
        chance_acerto=85,
        efeito_secundario="reduzir_defesa_alvo",
        valor_efeito=12
    ),
    "mordida_desdentada": Ataque(
        nome="Mordida Desdentada", 
        descricao="Um golpe fraco, porém preciso. Alta taxa de acerto crítico, reduz a defesa do alvo em 5.", 
        poder_base=20, 
        chance_acerto=100,
        chance_critico=40,
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
    "raio_de_gelo": Magia(
        nome="Raio de Gelo", 
        descricao="Lança um pulso de frio que reduz a defesa do alvo em 10.", 
        elemento="gelo",
        poder_base=35, 
        custo_mp=10,
        efeito_secundario="reduzir_defesa_alvo",
        valor_efeito=10
    ),
    "cura_basica": Magia(
        nome="Cura Básica", 
        descricao="Restaura uma quantidade moderada de HP de um aliado.", 
        elemento="cura", 
        poder_base=30, 
        custo_mp=15,
        alvo_aliado=True  # NOVO: Indica que o jogador deve escolher um alvo da party
    ),
    "pele_de_pedra": Magia(
        nome="Pele de Pedra", 
        descricao="Endurece a pele do alvo. Aumenta a defesa em 10 para o resto da batalha.", 
        elemento="terra", 
        poder_base=0, 
        custo_mp=12,
        efeito_secundario="aumentar_defesa_alvo",
        valor_efeito=10,
        alvo_aliado=True  # NOVO: Indica que o jogador deve escolher um alvo da party
    )
}