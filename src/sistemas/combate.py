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
    menu_escolher_alvo,
    menu_usar_item
)

def aplicar_efeitos_secundarios(alvo, habilidade):
    """Verifica e aplica efeitos secundários como redução ou aumento de defesa."""
    if hasattr(habilidade, 'efeito_secundario') and habilidade.efeito_secundario:
        if habilidade.efeito_secundario == "reduzir_defesa_alvo":
            alvo.defesa_atual = max(0, alvo.defesa_atual - habilidade.valor_efeito)
            print(f"    📉 A defesa de {alvo.nome} foi reduzida em {habilidade.valor_efeito}!")
        elif habilidade.efeito_secundario == "aumentar_defesa_alvo":
            alvo.defesa_atual += habilidade.valor_efeito
            print(f"    🛡️ A defesa de {alvo.nome} aumentou em {habilidade.valor_efeito}!")

def aplicar_item(usuario, alvo, item):
    """Aplica o efeito de um item consumível sobre o alvo e exibe o resultado."""
    if item.tipo_efeito == "cura_hp":
        cura = min(item.valor_efeito, alvo.hp_max - alvo.hp_atual)
        alvo.hp_atual += cura
        print(f"  💊 {usuario.nome} usou {item.nome} em {alvo.nome} e restaurou {cura} HP!")
    elif item.tipo_efeito == "cura_mp":
        cura = min(item.valor_efeito, alvo.mp_max - alvo.mp_atual)
        alvo.mp_atual += cura
        print(f"  💙 {usuario.nome} usou {item.nome} em {alvo.nome} e restaurou {cura} MP!")
    elif item.tipo_efeito == "buff_defesa":
        alvo.defesa_atual += item.valor_efeito
        alvo.defesa_base += item.valor_efeito 
        print(f"  🛡️  {usuario.nome} usou {item.nome} em {alvo.nome}! Defesa aumentou em {item.valor_efeito}!")

def iniciar_combate(party, inimigos):
    """Loop principal de uma batalha."""
    limpar_tela()
    exibir_cabecalho("ENCONTRO ALEATÓRIO")
    print("\n  ⚔️  Preparem-se para a batalha!\n")
    time.sleep(1.5)

    turno_numero = 1

    while True:
        # ==========================================
        # FASE 1: PLANEJAMENTO DA EQUIPE (JOGADOR)
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
                    if habilidade is None: continue
                    
                    alvo = menu_escolher_alvo(inimigos)
                    if alvo is None: continue
                    
                    fila_acoes.append({"ator": personagem, "habilidade": habilidade, "alvo": alvo, "tipo": "fisico"})
                    acao_confirmada = True
                    
                # [2] MAGIA
                elif escolha_acao == 2:
                    habilidade = menu_escolher_magia(personagem)
                    if habilidade is None: continue
                    
                    if habilidade.alvo_aliado:
                        print(f"\n  [Magia de Suporte] Escolha um aliado para {habilidade.nome}:")
                        alvo = menu_escolher_alvo(party) 
                        if alvo is None: continue
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
                    
                # [4] USAR ITEM
                elif escolha_acao == 4:
                    # Junta todo o inventário da equipe para exibir no menu
                    inventario_total = []
                    for membro in party:
                        for item in membro.inventario:
                            inventario_total.append((membro, item))

                    if not inventario_total:
                        print("\n  🎒 O inventário está vazio!")
                        time.sleep(1.5)
                        continue

                    resultado = menu_usar_item(personagem, party, inventario_total)
                    if resultado is None:
                        continue  # Jogador cancelou, volta ao menu de ações

                    dono, item, alvo = resultado
                    # Remove o item do inventário de quem o carregava
                    dono.inventario.remove(item)
                    # Registra a ação de item na fila (resolve na fase de resolução)
                    fila_acoes.append({"ator": personagem, "habilidade": None, "alvo": alvo, "tipo": "item", "item": item, "dono_item": dono})
                    acao_confirmada = True

        # ==========================================
        # FASE 2: PLANEJAMENTO INIMIGO (IA)
        # ==========================================
        for inimigo in inimigos:
            if inimigo.esta_vivo():
                inimigo.resetar_defesa()
                acao_inimiga = planejar_turno_inimigo(inimigo, party)
                if acao_inimiga:
                    acao_inimiga["ator"] = inimigo
                    fila_acoes.append(acao_inimiga)

        # ==========================================
        # FASE 3: INICIATIVA (ORDENAÇÃO)
        # ==========================================
        fila_acoes.sort(key=lambda acao: acao["ator"].agilidade, reverse=True)

        # ==========================================
        # FASE 4: RESOLUÇÃO DO TURNO (AÇÃO!)
        # ==========================================
        limpar_tela()
        exibir_cabecalho(f"RESOLUÇÃO DO TURNO {turno_numero}")
        print()
        
        for acao in fila_acoes:
            ator = acao["ator"]
            
            if not ator.esta_vivo():
                continue

            # Ação: DEFENDER
            if acao["tipo"] == "defesa":
                print(f"  🛡️  {ator.nome} assumiu uma postura defensiva!")
                time.sleep(1)
                continue

            # Ação: USAR ITEM
            if acao["tipo"] == "item":
                aplicar_item(ator, acao["alvo"], acao["item"])
                time.sleep(1.5)
                continue

            alvo = acao["alvo"]
            habilidade = acao["habilidade"]
            tipo = acao["tipo"]

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

            # Magias de Suporte (Buffs como Pele de Pedra)
            if tipo == "magico" and habilidade.efeito_secundario == "aumentar_defesa_alvo":
                if ator.gastar_mp(habilidade.custo_mp):
                    print(f"  ✨ {ator.nome} conjurou {habilidade.nome} em {alvo.nome}!")
                    aplicar_efeitos_secundarios(alvo, habilidade)
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

            if random.randint(1, 100) > habilidade.chance_acerto:
                print(f"  ❌ {ator.nome} usou {habilidade.nome}, mas errou o ataque!")
            else:
                dano, foi_critico, foi_fraqueza = calcular_dano(ator, alvo, habilidade, tipo)
                
                if foi_critico:
                    print("  🎯 ACERTO CRÍTICO!")
                if foi_fraqueza:
                    print("  🔥 ATAQUE SUPER EFETIVO!")
                    
                alvo.receber_dano(dano)
                print(f"  ⚔️  {ator.nome} usou {habilidade.nome} em {alvo.nome} e causou {dano} de dano!")
                
                aplicar_efeitos_secundarios(alvo, habilidade)

                if not alvo.esta_vivo():
                    print(f"  ☠️  {alvo.nome} foi derrotado!")

            time.sleep(1.5)

        # ==========================================
        # FASE 5: CHECAGEM DE FIM DE COMBATE
        # ==========================================
        party_viva = any(p.esta_vivo() for p in party)
        inimigos_vivos = any(i.esta_vivo() for i in inimigos)

        if not party_viva:
            print("\n  [!] A SUA EQUIPE FOI DIZIMADA...")
            time.sleep(2)
            return False
            
        elif not inimigos_vivos:
            print("\n  🎉 VITÓRIA! Todos os inimigos foram derrotados!")
            time.sleep(2)
            return True
            
        turno_numero += 1