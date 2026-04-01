"""
Módulo: combate.py
Descrição: Gerencia o fluxo de turnos, fila de ações e resolução de danos.
Totalmente integrado com a nova interface visual limpa.
"""

import random
import time

from src.sistemas.ia_inimiga import planejar_turno_inimigo
from src.utils.matematica import calcular_dano
from src.utils.interface import (
    limpar_tela, 
    exibir_cabecalho, 
    exibir_status_batalha, 
    menu_escolher_acao, 
    menu_escolher_ataque, 
    menu_escolher_magia, 
    menu_escolher_alvo
)

def aplicar_efeitos_secundarios(alvo, habilidade):
    """Verifica e aplica efeitos secundários como redução de defesa."""
    if hasattr(habilidade, 'efeito_secundario') and habilidade.efeito_secundario:
        if habilidade.efeito_secundario == "reduzir_defesa_alvo":
            alvo.defesa_atual = max(0, alvo.defesa_atual - habilidade.valor_efeito)
            print(f"    📉 A defesa de {alvo.nome} foi reduzida em {habilidade.valor_efeito}!")

def iniciar_combate(party, inimigos):
    """Loop principal de uma batalha."""
    limpar_tela()
    exibir_cabecalho("ENCONTRO ALEATÓRIO")
    print("\n  ⚔️  Preparem-se para a batalha!\n")
    time.sleep(1.5)

    turno_numero = 1

    while True:
        # ==========================================
        # FASE 1: PLANEAMENTO DA EQUIPA (JOGADOR)
        # ==========================================
        fila_acoes = []
        
        for personagem in party:
            if not personagem.esta_vivo():
                continue
                
            personagem.resetar_defesa()
            acao_confirmada = False
            
            while not acao_confirmada:
                limpar_tela()
                print(f"  --- TURNO {turno_numero} ---\n")
                exibir_status_batalha(party, inimigos)
                
                escolha_acao = menu_escolher_acao(personagem)
                
                # [1] ATACAR
                if escolha_acao == 1:
                    habilidade = menu_escolher_ataque(personagem)
                    if habilidade is None: continue # O jogador escolheu "Voltar"
                    
                    alvo = menu_escolher_alvo(inimigos)
                    if alvo is None: continue
                    
                    fila_acoes.append({"ator": personagem, "habilidade": habilidade, "alvo": alvo, "tipo": "fisico"})
                    acao_confirmada = True
                    
                # [2] MAGIA
                elif escolha_acao == 2:
                    habilidade = menu_escolher_magia(personagem)
                    if habilidade is None: continue
                    
                    # Se for magia de cura, o alvo é um aliado
                    if habilidade.elemento == "cura":
                        print("\n  [Magia de Suporte] Alvo automático: Aliado com menor HP.")
                        alvo = min([p for p in party if p.esta_vivo()], key=lambda p: p.hp_atual)
                        time.sleep(1.5)
                    else:
                        alvo = menu_escolher_alvo(inimigos)
                        if alvo is None: continue
                        
                    fila_acoes.append({"ator": personagem, "habilidade": habilidade, "alvo": alvo, "tipo": "magico"})
                    acao_confirmada = True
                    
                # [3] DEFENDER
                elif escolha_acao == 3:
                    personagem.acao_defender()
                    fila_acoes.append({"ator": personagem, "habilidade": None, "alvo": None, "tipo": "defesa"})
                    acao_confirmada = True
                    
                # [4] ITEM (Pode expandir no futuro)
                elif escolha_acao == 4:
                    print("\n  🎒 O inventário está vazio no momento!")
                    time.sleep(1.5)

        # ==========================================
        # FASE 2: PLANEAMENTO INIMIGO (IA)
        # ==========================================
        for inimigo in inimigos:
            if inimigo.esta_vivo():
                inimigo.resetar_defesa()
                acao_inimiga = planejar_turno_inimigo(inimigo, party)
                if acao_inimiga:
                    fila_acoes.append(acao_inimiga)

        # ==========================================
        # FASE 3: INICIATIVA (ORDENAÇÃO)
        # ==========================================
        # Ordena a fila de ações pela agilidade do ator (do mais rápido para o mais lento)
        fila_acoes.sort(key=lambda acao: acao["ator"].agilidade, reverse=True)

        # ==========================================
        # FASE 4: RESOLUÇÃO DO TURNO (AÇÃO!)
        # ==========================================
        limpar_tela()
        exibir_cabecalho(f"RESOLUÇÃO DO TURNO {turno_numero}")
        print() # Espaço para o log de batalha
        
        for acao in fila_acoes:
            ator = acao["ator"]
            
            # Se o ator morreu antes de chegar a sua vez, ele perde a ação
            if not ator.esta_vivo():
                continue

            # Se a ação foi "Defender"
            if acao["tipo"] == "defesa":
                print(f"  🛡️  {ator.nome} assumiu uma postura defensiva!")
                time.sleep(1)
                continue

            alvo = acao["alvo"]
            habilidade = acao["habilidade"]
            tipo = acao["tipo"]

            # Se o alvo morreu antes de receber o ataque
            if not alvo.esta_vivo():
                print(f"  💨 {ator.nome} tentou usar {habilidade.nome}, mas o alvo já estava caído!")
                time.sleep(1)
                continue

            # Magias de Cura
            if tipo == "magico" and habilidade.elemento == "cura":
                if ator.gastar_mp(habilidade.custo_mp):
                    cura = habilidade.poder_base + ator.inteligencia
                    alvo.hp_atual = min(alvo.hp_max, alvo.hp_atual + cura)
                    print(f"  ✨ {ator.nome} conjurou {habilidade.nome} e curou {cura} HP de {alvo.nome}!")
                else:
                    print(f"  💧 {ator.nome} tentou conjurar {habilidade.nome}, mas está sem MP!")
                time.sleep(1.5)
                continue

            # Ataques e Magias de Dano
            if tipo == "magico":
                if not ator.gastar_mp(habilidade.custo_mp):
                    print(f"  💧 {ator.nome} tentou usar {habilidade.nome}, mas está sem MP!")
                    time.sleep(1)
                    continue

            # Rolagem de chance de acerto
            if random.randint(1, 100) > habilidade.chance_acerto:
                print(f"  ❌ {ator.nome} usou {habilidade.nome}, mas errou o ataque!")
            else:
                # CORREÇÃO: Desempacotamento da tupla implementado aqui!
                dano, foi_critico, foi_fraqueza = calcular_dano(ator, alvo, habilidade, tipo)
                
                # Feedback visual
                if foi_critico:
                    print("  🎯 ACERTO CRÍTICO!")
                if foi_fraqueza:
                    print("  🔥 ATAQUE SUPER EFETIVO!")
                    
                alvo.receber_dano(dano)
                print(f"  ⚔️  {ator.nome} usou {habilidade.nome} em {alvo.nome} e causou {dano} de dano!")
                
                # Aplica quebra de escudos, buffs, etc.
                aplicar_efeitos_secundarios(alvo, habilidade)

                if not alvo.esta_vivo():
                    print(f"  ☠️  {alvo.nome} foi derrotado!")

            time.sleep(1.5) # Pausa dramática para o jogador ler o texto

        # ==========================================
        # FASE 5: CHECAGEM DE FIM DE COMBATE
        # ==========================================
        party_viva = any(p.esta_vivo() for p in party)
        inimigos_vivos = any(i.esta_vivo() for i in inimigos)

        if not party_viva:
            print("\n  [!] A SUA EQUIPA FOI DIZIMADA...")
            time.sleep(2)
            return False
            
        elif not inimigos_vivos:
            print("\n  🎉 VITÓRIA! Todos os inimigos foram derrotados!")
            time.sleep(2)
            return True
            
        turno_numero += 1