"""
Módulo: ia_inimiga.py
Descrição: Gerencia a tomada de decisão dos inimigos durante a fase de planejamento do combate.
"""

import random

def calcular_resistencia(personagem):
    """
    Calcula a resistência de um alvo com base na soma do seu HP atual e Defesa atual.
    """
    return personagem.hp_atual + personagem.defesa_atual

def escolher_alvo(inimigo, party):
    """
    Define quem o inimigo vai atacar.
    Usa a chance específica do inimigo para focar no membro de menor resistência,
    ou escolhe um alvo aleatório entre os vivos.
    """
    # Filtra apenas os membros da party que ainda estão vivos
    alvos_vivos = [membro for membro in party if membro.esta_vivo()]
    
    if getattr(inimigo, 'chance_focar_fraco', 20) >= random.randint(1, 100):
        # Encontra o personagem com o menor valor de (hp + defesa)
        alvo_escolhido = min(alvos_vivos, key=calcular_resistencia)
    else:
        # Escolhe um alvo aleatório
        alvo_escolhido = random.choice(alvos_vivos)
        
    return alvo_escolhido

def escolher_habilidade(inimigo):
    """
    Define qual ataque ou magia o inimigo usará.
    Garante que ele só escolha magias se tiver MP suficiente.
    """
    # Junta todos os ataques e magias possíveis
    habilidades_disponiveis = []
    habilidades_disponiveis.extend(inimigo.ataques)
    
    for magia in inimigo.magias:
        if inimigo.mp_atual >= magia.custo_mp:
            habilidades_disponiveis.append(magia)
            
    # Se por algum motivo o inimigo não tiver nada, retorna None (vai pular a vez ou usar ataque base)
    if not habilidades_disponiveis:
        return None
        
    if getattr(inimigo, 'chance_usar_forte', 60) >= random.randint(1, 100):
        # Escolhe a habilidade com o maior poder_base
        habilidade_escolhida = max(habilidades_disponiveis, key=lambda hab: hab.poder_base)
    else:
        # Escolhe qualquer habilidade válida aleatoriamente
        habilidade_escolhida = random.choice(habilidades_disponiveis)
        
    return habilidade_escolhida

def planejar_turno_inimigo(inimigo, party):
    """
    Função principal chamada pelo combate.py.
    Retorna um dicionário contendo a ação que o inimigo decidiu tomar.
    """
    alvo = escolher_alvo(inimigo, party)
    habilidade = escolher_habilidade(inimigo)
    
    # Se o inimigo não conseguir agir (ex: atordoado ou sem opções), pula a vez
    if habilidade is None:
        return None
        
    # Descobre se a habilidade escolhida é uma magia ou um ataque físico
    tipo_acao = "magico" if habilidade in inimigo.magias else "fisico"
    
    # Retorna o dicionário de ação completo, AGORA COM A CHAVE 'tipo'!
    return {
        "ator": inimigo, 
        "habilidade": habilidade, 
        "alvo": alvo, 
        "tipo": tipo_acao
    }