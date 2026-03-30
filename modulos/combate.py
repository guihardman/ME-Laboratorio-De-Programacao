def calcular_dano_fisico(ataque: int, defesa: int) -> int:
   
    if ataque < 0 or defesa < 0:
        raise ValueError("Ataque e defesa não podem ser números negativos.")
    
    dano_final = ataque - defesa
   
    return max(0, dano_final)


def calcular_acerto_critico(dano_base: int, chance_critico: int, rolagem_dado: int) -> int:
   
    if dano_base < 0:
        raise ValueError("O dano base não pode ser negativo.")
        
    if rolagem_dado <= chance_critico:
        return dano_base * 2  
    
    return dano_base


def verificar_esquiva(agilidade_defensor: int, rolagem_dado: int) -> bool:
   
    chance_esquiva = min(agilidade_defensor * 2, 80)
    
    return rolagem_dado <= chance_esquiva