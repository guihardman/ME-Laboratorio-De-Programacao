def consumir_mana(personagem: dict, custo_mp: int) -> None:

    # Desconta o custo de mana do personagem.
    # Se ele não tiver mana suficiente, levanta um erro.


    if personagem['mp_atual'] < custo_mp:
        raise ValueError("Mana insuficiente para conjurar a magia!")

    # Se passou da validação, o código continua e desconta a mana
    personagem['mp_atual'] -= custo_mp


def calcular_dano_magico(poder_magico: int, resistencia_magica: int) -> int:

    # Calcula o estrago do feitiço. A resistência reduz o impacto.

    if poder_magico < 0 or resistencia_magica < 0:
        raise ValueError("Poder e resistência não podem ser negativos.")

    dano_final = poder_magico - resistencia_magica
    return max(0, dano_final)  # Se o dano final for negativo, retorna 0.


def recuperar_mana(personagem: dict, quantidade: int) -> None:

    # Aumenta a mana atual, mas nunca permite passar do mp_maximo.
    
    if quantidade <= 0:
        return  # Não faz nada se tentar curar zero ou negativo

    nova_mana = personagem['mp_atual'] + quantidade

    # O min() vai escolher o menor valor.
    personagem['mp_atual'] = min(nova_mana, personagem['mp_maximo'])