def criar_personagem(nome: str, hp_maximo: int, ataque: int, defesa: int) -> dict:
    """Fábrica que cria o dicionário do personagem."""
    
    # Validação de segurança (Vida não pode ser 0 ou negativa)
    if hp_maximo <= 0:
        raise ValueError("O HP máximo de um personagem deve ser maior que zero.")
    
    # Cria e retorna o dicionário
    return {
        "nome": nome,
        "hp_maximo": hp_maximo,
        "hp_atual": hp_maximo, 
        "ataque": ataque,
        "defesa": defesa
    }

def aplicar_dano(personagem: dict, quantidade_dano: int) -> None:
    """Reduz o HP do personagem, travando em zero se o dano for fatal."""
    
    # Se o dano for negativo (erro externo), não faz nada
    if quantidade_dano < 0:
        return

    # Subtrai o dano da vida atual
    personagem["hp_atual"] -= quantidade_dano
    
    # Trava de segurança: se a vida caiu abaixo de zero, nós forçamos a ser zero.
    if personagem["hp_atual"] < 0:
        personagem["hp_atual"] = 0

def esta_vivo(personagem: dict) -> bool:
    """Retorna True se o personagem tiver vida maior que 0."""
    return personagem["hp_atual"] > 0