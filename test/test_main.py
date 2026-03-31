import unittest

from main import criar_barra

class TestMain(unittest.TestCase):

    def test_criar_barra_metade(self):
        """Verifica se a barra preenche exatamente a metade."""
        # Ex: 5 de 10 com tamanho 10 deve gerar 5 blocos cheios e 5 vazios
        resultado = criar_barra(valor_atual=5, valor_maximo=10, tamanho=10)
        self.assertEqual(resultado, "[█████░░░░░]")

    def test_criar_barra_cheia(self):
        """Verifica se a barra fica 100% cheia no HP máximo."""
        resultado = criar_barra(valor_atual=10, valor_maximo=10, tamanho=10)
        self.assertEqual(resultado, "[██████████]")

    def test_criar_barra_vazia(self):
        """Verifica se a barra fica 0% quando o HP chega a zero."""
        resultado = criar_barra(valor_atual=0, valor_maximo=10, tamanho=10)
        self.assertEqual(resultado, "[░░░░░░░░░░]")

    def test_criar_barra_acima_do_maximo(self):
        """Garante que a barra não 'quebra' visualmente se o HP passar do máximo."""
        resultado = criar_barra(valor_atual=15, valor_maximo=10, tamanho=10)
        self.assertEqual(resultado, "[██████████]")

    def test_criar_barra_vida_negativa(self):
        """Garante que a barra não tenta desenhar blocos negativos se o HP bugar para -5."""
        resultado = criar_barra(valor_atual=-5, valor_maximo=10, tamanho=10)
        self.assertEqual(resultado, "[░░░░░░░░░░]")

    def test_criar_barra_evita_divisao_por_zero(self):
        """Testa a trava de segurança caso um inimigo seja criado com 0 de HP máximo."""
        resultado = criar_barra(valor_atual=0, valor_maximo=0, tamanho=10)
        self.assertEqual(resultado, "[░░░░░░░░░░]")

if __name__ == '__main__':
    unittest.main()