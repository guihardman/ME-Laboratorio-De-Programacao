MAGIAS_DISPONIVEIS = {
    "bola de fogo": {"custo_mp": 15, "poder_base": 30, "tipo": "dano"},
    "raio de gelo": {"custo_mp": 10, "poder_base": 20, "tipo": "dano"},
    "luz divina": {"custo_mp": 12, "poder_base": 25, "tipo": "cura"}
}

CLASSES_DISPONIVEIS = {
    "guerreiro": {
        "hp_maximo": 120, "mp_maximo": 20, "ataque": 50, "defesa": 20,
        "poder_magico": 5, "resistencia_magica": 10, "velocidade": 12,
        "magias": ["luz divina"]
    },
    "mago": {
        "hp_maximo": 80, "mp_maximo": 60, "ataque": 20, "defesa": 5,
        "poder_magico": 35, "resistencia_magica": 20, "velocidade": 15,
        "magias": ["bola de fogo", "raio de gelo"]
    },
    "paladino": {
        "hp_maximo": 100, "mp_maximo": 40, "ataque": 30, "defesa": 15,
        "poder_magico": 20, "resistencia_magica": 15, "velocidade": 10,
        "magias": ["luz divina", "raio de gelo"]
    }
}