"""
Módulo: itens.py
Descrição: Define a classe de itens consumíveis e armazena o catálogo 
de itens que podem ser coletados no mapa e usados no combate.
"""

class ItemConsumivel:
    """
    Representa um item que pode ser usado uma vez e depois é removido do inventário.
    """
    def __init__(self, nome, descricao, tipo_efeito, valor_efeito):
        self.nome = nome
        self.descricao = descricao
        
        # O tipo de efeito diz ao sistema de combate o que este item altera
        # Ex: 'cura_hp', 'cura_mp', 'buff_forca', 'buff_defesa'
        self.tipo_efeito = tipo_efeito 
        
        # O valor numérico do efeito (ex: quanto de HP cura, ou quanto de Força aumenta)
        self.valor_efeito = valor_efeito


# ==========================================
#           CATÁLOGO DE ITENS
# ==========================================

CATALOGO_ITENS = {
    "pocao_vida_menor": ItemConsumivel(
        nome="Poção de Vida Menor",
        descricao="Um frasco com um líquido vermelho. Restaura 50 de HP.",
        tipo_efeito="cura_hp",
        valor_efeito=50
    ),
    "pocao_vida_maior": ItemConsumivel(
        nome="Poção de Vida Maior",
        descricao="Um frasco grande e brilhante. Restaura 150 de HP.",
        tipo_efeito="cura_hp",
        valor_efeito=150
    ),
    "pocao_mana_menor": ItemConsumivel(
        nome="Poção de Mana Menor",
        descricao="Um líquido azul cintilante. Restaura 30 de MP.",
        tipo_efeito="cura_mp",
        valor_efeito=30
    ),
    "elixir_de_ferro": ItemConsumivel(
        nome="Elixir de Ferro",
        descricao="Uma poção densa. Aumenta a Defesa em 15 pontos temporariamente.",
        tipo_efeito="buff_defesa",
        valor_efeito=15
    )
}