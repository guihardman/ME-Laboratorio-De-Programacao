import random

def rolar_chance(porcentagem):
    """
    Rola um 'dado' de 100 faces virtual. 
    Retorna True se o resultado for menor ou igual à porcentagem informada.
    """
    return random.randint(1, 100) <= porcentagem


def calcular_dano(ator, alvo, habilidade, tipo="fisico"):
    """
    Calcula o dano final considerando ataque/magia, atributos e a defesa atual do alvo.
    
    Retorna:
        tuple: (dano_final, foi_critico, foi_fraqueza)
    """
    dano_base = habilidade.poder_base
    foi_critico = False
    foi_fraqueza = False
    
    if tipo == "fisico":
        # Dano físico escala com o atributo Força
        dano_bruto = ator.forca + dano_base
        
        # Checa se o golpe foi crítico
        if rolar_chance(habilidade.chance_critico):
            foi_critico = True
            dano_bruto *= 2  # O dano dobra antes de subtrair a armadura
            
    else: 
        # Dano mágico escala com o atributo Inteligência
        dano_bruto = ator.inteligencia + dano_base
        
        # Checa a fraqueza elemental do inimigo
        if hasattr(alvo, 'fraqueza') and alvo.fraqueza == habilidade.elemento:
            foi_fraqueza = True
            dano_bruto *= 2  # O dano mágico dobra caso atinja uma fraqueza
            
    # A defesa atual (que pode estar fortalecida pelo comando "Defender") reduz o dano bruto
    dano_final = dano_bruto - alvo.defesa_atual
    
    # Retorna o dano final garantindo que nunca seja negativo (graças ao max(0, ...))
    return max(0, dano_final), foi_critico, foi_fraqueza