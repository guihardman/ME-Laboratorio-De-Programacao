def consumir_mana(personagem: dict, custo_mp: int) -> None:
    """
    Desconta o custo de mana do personagem.

    Parâmetros:
        personagem (dict): Dicionário representando o personagem (deve conter 'mp_atual').
        custo_mp (int): Quantidade de mana a ser consumida.

    Levanta:
        ValueError: Caso o personagem não tiver mana suficiente.
    """
    if personagem['mp_atual'] < custo_mp:
        raise ValueError("Mana insuficiente para conjurar a magia!")

    # Se passou da validação, o código continua e desconta a mana
    personagem['mp_atual'] -= custo_mp


def calcular_dano_magico(poder_magico: int, resistencia_magica: int) -> int:
    """
    Calcula o estrago do feitiço. A resistência reduz o impacto.

    Parâmetros:
        poder_magico (int): O poder do feitiço conjurado.
        resistencia_magica (int): A defesa mágica do alvo.

    Retorna:
        int: O dano final causado. Se o dano final for negativo, retorna 0.

    Levanta:
        ValueError: Se poder ou resistência forem negativos.
    """
    if poder_magico < 0 or resistencia_magica < 0:
        raise ValueError("Poder e resistência não podem ser negativos.")

    dano_final = poder_magico - resistencia_magica
    return max(0, dano_final)


def recuperar_mana(personagem: dict, quantidade: int) -> None:
    """
    Aumenta a mana atual, mas nunca permite passar do limite de mp_maximo.

    Parâmetros:
        personagem (dict): Dicionário representando o personagem (deve conter 'mp_atual' e 'mp_maximo').
        quantidade (int): A quantidade de mana a ser recuperada.
    """
    if quantidade <= 0:
        return  # Não faz nada se tentar curar zero ou negativo

    nova_mana = personagem['mp_atual'] + quantidade

    # O min() vai escolher o menor valor.
    personagem['mp_atual'] = min(nova_mana, personagem['mp_maximo'])