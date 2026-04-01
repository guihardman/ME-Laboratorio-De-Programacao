"""
Módulo: matematica.py
Descrição: Centraliza todos os cálculos de combate, rolagens de probabilidade e
estatísticas. Mantém a lógica pura separada da interface e do fluxo do jogo.
"""

import random

def rolar_chance(porcentagem):
    """
    Rola um 'dado' de 100 faces virtual. 
    Retorna True se o resultado for menor ou igual à porcentagem informada.
    """
    return random.randint(1, 100) <= porcentagem

def calcular_dano(ator, alvo, habilidade, tipo="fisico"):
    """
    Calcula o dano final considerando ataque/magia, atributos e defesa atual.
    Retorna uma tupla contendo: (dano_final, foi_critico, foi_fraqueza)
    """
    dano_base = habilidade.poder_base
    foi_critico = False
    foi_fraqueza = False
    
    if tipo == "fisico":
        # Dano físico usa a Força
        dano_bruto = ator.forca + dano_base
        
        # Checa se o golpe foi crítico
        if rolar_chance(habilidade.chance_critico):
            foi_critico = True
            dano_bruto *= 2  # Dano dobra antes da armadura
            
    else: 
        # Dano mágico usa a Inteligência
        dano_bruto = ator.inteligencia + dano_base
        
        # Checa fraqueza elemental do inimigo
        if hasattr(alvo, 'fraqueza') and alvo.fraqueza == habilidade.elemento:
            foi_fraqueza = True
            dano_bruto *= 2  # Dano dobra antes da armadura

    # A defesa atual (que pode estar buffada pelo comando Defender) reduz o dano
    dano_final = dano_bruto - alvo.defesa_atual
    
    # Retorna o dano final (garantindo que não seja negativo) e os status do ataque
    return max(0, dano_final), foi_critico, foi_fraqueza

def calcular_resistencia(personagem):
    """
    Calcula o quão 'tanque' um personagem está no momento.
    Usado pela IA inimiga para descobrir quem é o alvo mais vulnerável.
    """
    return personagem.hp_atual + personagem.defesa_atual