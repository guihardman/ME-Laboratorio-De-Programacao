import sys
from src.jogo import main as iniciar_rpg
from src.utils.interface import limpar_tela, exibir_cabecalho

def executar_jogo():
    """
    Função que encapsula a execução para capturar erros fatais
    e garantir uma saída limpa para o usuário.
    """
    try:
        # Tenta iniciar o loop principal do jogo
        iniciar_rpg()
        
    except KeyboardInterrupt:
        # Caso o usuário aperte Ctrl+C, o jogo fecha elegantemente
        print("\n\n[SISTEMA] O jogo foi encerrado pelo usuário.")
        sys.exit(0)
        
    except Exception as e:
        # Caso ocorra um erro de programação inesperado, a tela é limpa
        # e uma mensagem "amigável" é exibida.
        limpar_tela()
        exibir_cabecalho("ERRO CRÍTICO")
        print(f"Ocorreu um erro inesperado: {e}")
        print("\nPor favor, contate o suporte técnico (não reduza nossa nota).")
        input("\nPressione ENTER para sair...")
        sys.exit(1)

if __name__ == "__main__":
    executar_jogo()
