def adicionar_item(inventario: list, item: str) -> None:
    """Adiciona um novo item à lista de inventário."""
    inventario.append(item)


def remover_item(inventario: list, item: str) -> None:
    #"""Remove um item da lista. Levanta erro se o item não existir."""

    # Verifica se o item NÃO está na lista
    if item not in inventario:
        raise ValueError(f"O item '{item}' não existe no inventário.")

    # Se passou da verificação, remove com segurança
    inventario.remove(item)


def usar_pocao_cura(personagem: dict, valor_cura: int) -> None:
    """
    Aumenta o HP atual. Trava no HP Máximo.
    Levanta erro se o personagem estiver com 0 de HP ou menos.
    """
    if personagem['hp_atual'] <= 0:
        raise ValueError("Não é possível curar um personagem que já está morto.")

    # Aplica a cura
    personagem['hp_atual'] += valor_cura

    # Trava a vida no limite máximo (o famoso "cap")
    personagem['hp_atual'] = min(personagem['hp_atual'], personagem['hp_maximo'])