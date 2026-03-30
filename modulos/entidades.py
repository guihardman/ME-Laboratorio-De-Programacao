from modulos.dados import CLASSES_DISPONIVEIS

def criar_personagem(nome: str, classe_escolhida: str) -> dict:
    """Fábrica que cria o personagem baseado na classe."""
    
    classe_formatada = classe_escolhida.lower().strip()
    if classe_formatada not in CLASSES_DISPONIVEIS:
        raise ValueError(f"A classe '{classe_escolhida}' não existe!")
    
    # Puxa os status baseados na classe
    status = CLASSES_DISPONIVEIS[classe_formatada]
    
    return {
        "nome": nome,
        "classe": classe_formatada.capitalize(),
        "hp_maximo": status["hp_maximo"],
        "hp_atual": status["hp_maximo"],
        "mp_maximo": status["mp_maximo"],
        "mp_atual": status["mp_maximo"],
        "ataque": status["ataque"],
        "defesa": status["defesa"],
        "poder_magico": status["poder_magico"],
        "resistencia_magica": status["resistencia_magica"],
        "velocidade": status["velocidade"],
        "magias": status["magias"]
    }

def aplicar_dano(personagem: dict, quantidade_dano: int) -> None:
    """Reduz o HP do personagem, travando em zero se o dano for fatal."""
    
    # Se o dano for negativo (erro externo), não faz nada
    if quantidade_dano < 0:
        return

    # Subtrai o dano da vida atual
    personagem["hp_atual"] -= quantidade_dano
    
    # Trava de segurança: se a vida caiu abaixo de zero, força a ser zero.
    if personagem["hp_atual"] < 0:
        personagem["hp_atual"] = 0

def esta_vivo(personagem: dict) -> bool:
    """Retorna True se o personagem tiver vida maior que 0."""
    return personagem["hp_atual"] > 0