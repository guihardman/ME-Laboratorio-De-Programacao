import unittest

from modulos.magia import consumir_mana, calcular_dano_magico, recuperar_mana

class TestMagia(unittest.TestCase):
    """Conjunto de testes para as funções do módulo de magia."""

    def test_consumir_mana_com_sucesso(self):
        """Testa se a mana é descontada corretamente quando o personagem tem o suficiente."""
        mago = {'mp_atual': 50, 'mp_maximo': 100}
        consumir_mana(mago, custo_mp=20)
        self.assertEqual(mago['mp_atual'], 30)

    def test_consumir_mana_sem_ter_o_suficiente(self):
        """Testa se levanta ValueError quando o custo é maior que a mana atual."""
        mago = {'mp_atual': 5, 'mp_maximo': 100}
        with self.assertRaises(ValueError):
            consumir_mana(mago, custo_mp=50)

    def test_dano_magico_normal(self):
        """Testa se o cálculo de dano deduz a resistência mágica corretamente."""
        resultado = calcular_dano_magico(poder_magico=100, resistencia_magica=30)
        self.assertEqual(resultado, 70)

    def test_recuperar_mana_trava_no_maximo(self):
        """Testa se a recuperação de mana respeita o teto de 'mp_maximo'."""
        mago = {'mp_atual': 90, 'mp_maximo': 100}
        recuperar_mana(mago, quantidade=50)
        self.assertEqual(mago['mp_atual'], 100)


if __name__ == '__main__':
    unittest.main()