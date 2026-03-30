import unittest

from modulos.magia import consumir_mana, calcular_dano_magico, recuperar_mana


class TestMagia(unittest.TestCase):

    # Teste do consumo
    def test_consumir_mana_com_sucesso(self):
        # Boneco de teste com 50 de mana
        mago = {'mp_atual': 50, 'mp_maximo': 100}

        consumir_mana(mago, custo_mp=20)
        # O teste vai passar se a mana do mago cair de 50 para 30
        self.assertEqual(mago['mp_atual'], 30)

    def test_consumir_mana_sem_ter_o_suficiente(self):
        # Teste com mana baixa
        mago = {'mp_atual': 5, 'mp_maximo': 100}

        # Como a magia custa 50 e ele só tem 5, irá resultar no erro ValueError
        with self.assertRaises(ValueError):
            consumir_mana(mago, custo_mp=50)

    # Teste do Cálculo de Dano
    def test_dano_magico_normal(self):
        # Dano de 100 contra 30 de defesa mágica tem que sobrar 70
        resultado = calcular_dano_magico(poder_magico=100, resistencia_magica=30)
        self.assertEqual(resultado, 70)

    # Teste da recuperação de mana
    def test_recuperar_mana_trava_no_maximo(self):

        mago = {'mp_atual': 90, 'mp_maximo': 100}

        # Tenta recuperar 50. A matemática daria 140, mas a regra manda travar em 100
        recuperar_mana(mago, quantidade=50)
        self.assertEqual(mago['mp_atual'], 100)


if __name__ == '__main__':
    unittest.main()