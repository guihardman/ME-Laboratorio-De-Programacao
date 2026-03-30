def adicionar_item(inventario: list, item: str) -> None:

    inventario.append(item)


def remover_item(inventario: list, item: str) -> None:

    if item not in inventario:
        raise ValueError(f"O item '{item}' não existe no inventário.")

    inventario.remove(item)


def usar_pocao_cura(personagem: dict, valor_cura: int) -> None:

    if personagem['hp_atual'] <= 0:
        raise ValueError("Não é possível curar um personagem que já está morto.")

    personagem['hp_atual'] += valor_cura
    personagem['hp_atual'] = min(personagem['hp_atual'], personagem['hp_maximo'])