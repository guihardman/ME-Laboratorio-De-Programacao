def calcular_dano_fisico(ataque: int, defesa: int) -> int:
    """
    Calcula o dano físico final causado a um alvo, considerando sua defesa.

    Parâmetros:
        ataque (int): O valor de ataque do agressor.
        defesa (int): O valor de defesa do alvo.

    Retorna:
        int: O dano final a ser aplicado. Retorna 0 se a defesa for maior que o ataque.

    Levanta:
        ValueError: Se os valores de ataque ou defesa forem menores que zero.
    """
    if ataque < 0 or defesa < 0:
        raise ValueError("Ataque e defesa não podem ser números negativos.")
    
    dano_final = ataque - defesa
   
    return max(0, dano_final)


def calcular_acerto_critico(dano_base: int, chance_critico: int, rolagem_dado: int) -> int:
    """
    Verifica se um ataque foi crítico com base em uma rolagem de dados e dobra o dano se for o caso.

    Parâmetros:
        dano_base (int): O valor do dano antes de calcular o crítico.
        chance_critico (int): O valor alvo (porcentagem/chance) para o crítico ocorrer.
        rolagem_dado (int): O resultado do dado rolado pelo sistema (ex: 1 a 100).

    Retorna:
        int: O dano dobrado se o dado for menor ou igual à chance de crítico; caso contrário, o dano base.

    Levanta:
        ValueError: Se o dano base fornecido for negativo.
    """
    if dano_base < 0:
        raise ValueError("O dano base não pode ser negativo.")
        
    if rolagem_dado <= chance_critico:
        return dano_base * 2  
    
    return dano_base


def verificar_esquiva(agilidade_defensor: int, rolagem_dado: int) -> bool:
    """
    Determina se o defensor conseguiu esquivar do ataque baseado em sua agilidade.

    A chance de esquiva é o dobro da agilidade do defensor, com um limite máximo (cap) de 80%.

    Parâmetros:
        agilidade_defensor (int): O atributo de agilidade do personagem que está se defendendo.
        rolagem_dado (int): O resultado do dado rolado pelo sistema (ex: 1 a 100).

    Retorna:
        bool: True se o defensor conseguiu se esquivar (dado menor ou igual à chance), False caso contrário.
    """
    chance_esquiva = min(agilidade_defensor * 2, 80)
    
    return rolagem_dado <= chance_esquiva