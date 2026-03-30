import random

from modulos.combate import calcular_dano_fisico
from modulos.entidades import aplicar_dano, esta_vivo
from modulos.inventario import usar_pocao_cura
from modulos.magia import consumir_mana, calcular_dano_magico
from modulos.dados import MAGIAS_DISPONIVEIS

def determinar_iniciativa(velocidade_p: int, velocidade_inimigo: int) -> str:
    """Retorna 'p' se o jogador for mais rápido, ou 'inimigo' se o inimigo for. Desempata na moeda."""
    if velocidade_p > velocidade_inimigo:
        return 'p'
    elif velocidade_inimigo > velocidade_p:
        return 'inimigo'
    else:
        return random.choice(['p', 'inimigo'])
    
def verificar_vencedor(jogador: dict, inimigo: dict) -> str:
    """Verifica quem está vivo e retorna o status da partida."""
    jogador_vivo = esta_vivo(jogador)
    inimigo_vivo = esta_vivo(inimigo)

    if jogador_vivo and inimigo_vivo:
        return "Andamento"
    elif jogador_vivo and not inimigo_vivo:
        return "Jogador"
    elif not jogador_vivo and inimigo_vivo:
        return "Inimigo"
    else:
        return "Empate"
    
def executar_acao(atacante: dict, defensor: dict, tipo_acao: str, nome_magia: str = "") -> None:
    """Lê a intenção de ação e orquestra a chamada das funções corretas."""
    
    acoes_validas = ['atacar', 'curar', 'magia']
    if tipo_acao not in acoes_validas:
        raise ValueError(f"Ação desconhecida: '{tipo_acao}'.")

    if tipo_acao == 'atacar':
        dano = calcular_dano_fisico(ataque=atacante['ataque'], defesa=defensor['defesa'])
        aplicar_dano(personagem=defensor, quantidade_dano=dano)

    elif tipo_acao == 'curar':
        usar_pocao_cura(personagem=atacante, valor_cura=30)
        
    elif tipo_acao == 'magia':
        # 1. Verifica se a magia existe e se o personagem sabe usá-la
        magia_formatada = nome_magia.lower().strip()
        if magia_formatada not in atacante['magias']:
            raise ValueError(f"O personagem não conhece a magia '{nome_magia}'.")
            
        dados_magia = MAGIAS_DISPONIVEIS[magia_formatada]
        
        # 2. Gasta a mana (levanta erro se não tiver suficiente)
        consumir_mana(personagem=atacante, custo_mp=dados_magia["custo_mp"])
        
        # 3. Aplica o efeito (Dano ou Cura)
        if dados_magia["tipo"] == "dano":
            poder_total = dados_magia["poder_base"] + atacante['poder_magico']
            dano_magico = calcular_dano_magico(poder_magico=poder_total, resistencia_magica=defensor['resistencia_magica'])
            aplicar_dano(personagem=defensor, quantidade_dano=dano_magico)
        elif dados_magia["tipo"] == "cura":
            usar_pocao_cura(personagem=atacante, valor_cura=dados_magia["poder_base"])