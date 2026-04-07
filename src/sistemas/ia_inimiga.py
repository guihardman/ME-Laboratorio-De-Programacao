import random


def calcular_resistencia(personagem):
    """
    Calcula a resistência de um alvo com base na soma do seu HP atual e Defesa atual.
    """
    return personagem.hp_atual + personagem.defesa_atual


def escolher_alvo(inimigo, equipe):
    """
    Define quem o inimigo vai atacar.
    Usa a chance específica do inimigo para focar no membro de menor resistência,
    ou escolhe um alvo aleatório entre os vivos.
    """
    alvos_vivos = [membro for membro in equipe if membro.esta_vivo()]
    
    if getattr(inimigo, 'chance_focar_fraco', 20) >= random.randint(1, 100):
        alvo_escolhido = min(alvos_vivos, key=calcular_resistencia)
    else:
        alvo_escolhido = random.choice(alvos_vivos)
        
    return alvo_escolhido


def escolher_habilidade(inimigo):
    """
    Define qual ataque ou magia o inimigo usará.
    Garante que ele só escolha magias se tiver MP suficiente.
    """
    habilidades_disponiveis = []
    habilidades_disponiveis.extend(inimigo.ataques)
    
    for magia in inimigo.magias:
        if inimigo.mp_atual >= magia.custo_mp:
            habilidades_disponiveis.append(magia)
            
    if not habilidades_disponiveis:
        return None
        
    if getattr(inimigo, 'chance_usar_forte', 60) >= random.randint(1, 100):
        habilidade_escolhida = max(habilidades_disponiveis, key=lambda hab: hab.poder_base)
    else:
        habilidade_escolhida = random.choice(habilidades_disponiveis)
        
    return habilidade_escolhida


def planejar_turno_inimigo(inimigo, equipe):
    """
    Função principal chamada pelo combate.py.
    Retorna um dicionário contendo a ação que o inimigo decidiu tomar,
    incluindo a chave 'ator' necessária para a ordenação por iniciativa.
    """
    alvo = escolher_alvo(inimigo, equipe)
    habilidade = escolher_habilidade(inimigo)
    
    if habilidade is None:
        return None
        
    tipo_acao = "magico" if habilidade in inimigo.magias else "fisico"
    
    return {
        "ator": inimigo,          # CORREÇÃO: chave 'ator' incluída aqui na origem
        "tipo": "habilidade",
        "habilidade": habilidade,
        "tipo_habilidade": tipo_acao,
        "alvo": alvo
    }