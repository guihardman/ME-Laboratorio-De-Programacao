import random

from modulos.entidades import aplicar_dano, esta_vivo
from modulos.combate import calcular_dano_fisico
from modulos.magia import consumir_mana, calcular_dano_magico
from modulos.inventario import usar_pocao_cura

def determinar_iniciativa(velocidade_p: int, velocidade_mob: int) -> str:
    """Retorna 'p' se o jogador for mais rápido, ou 'mob' se o inimigo for. Desempata na moeda."""
    if velocidade_p > velocidade_mob:
        return 'p'
    elif velocidade_mob > velocidade_p:
        return 'mob'
    else:
        return random.choice(['p', 'mob'])
    
def verificar_vencedor(jogador: dict, inimigo: dict) -> str:
    """Verifica quem está vivo e retorna o status da partida."""
    jogador_vivo = esta_vivo(jogador)
    inimigo_vivo = esta_vivo(inimigo)

    if jogador_vivo and inimigo_vivo:
        return "Andamento" # Ninguém morreu ainda, o jogo continua
    elif jogador_vivo and not inimigo_vivo:
        return "Jogador"   # Inimigo morreu, jogador ganha
    elif not jogador_vivo and inimigo_vivo:
        return "Inimigo"   # Jogador morreu, tela de Game Over
    else:
        return "Empate"
    
def executar_acao(atacante: dict, defensor: dict, tipo_acao: str) -> None:
    """Lê a intenção de ação e orquestra a chamada das funções corretas."""
    
    # 1. VALIDAÇÃO
    acoes_validas = ['atacar', 'curar', 'magia']
    if tipo_acao not in acoes_validas:
        raise ValueError(f"Ação desconhecida: '{tipo_acao}'. As regras não permitem isso.")

    # 2. ROTEAMENTO
    if tipo_acao == 'atacar':
        # Passo A: Acessa combate.py e calcula o dano
        dano = calcular_dano_fisico(ataque=atacante['ataque'], defesa=defensor['defesa'])
        # Passo B: Acessa entidades.py e arranca essa quantidade de vida do defensor
        aplicar_dano(personagem=defensor, quantidade_dano=dano)

    elif tipo_acao == 'curar':
        # Acessa inventario.py e cura 30 pontos de vida do atacante
        usar_pocao_cura(personagem=atacante, valor_cura=30)
        
    elif tipo_acao == 'magia':
        # Acessa magia.py para gastar os mp e castar a magia
        consumir_mana(personagem=atacante, custo_mp=10)
        dano_magico = calcular_dano_magico(poder_magico=atacante['poder_magico'], resistencia_magica=defensor['resistencia_magica'])
        aplicar_dano(personagem=defensor, quantidade_dano=dano_magico)