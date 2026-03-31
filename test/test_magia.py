import unittest

from modulos.magia import consumir_mana, calcular_dano_magico, recuperar_mana

class TestMagia(unittest.TestCase):

    # Testes da função consumir_mana

    def test_consumir_mana_sucesso(self):
        """Verifica se a mana é descontada corretamente quando há saldo suficiente."""
        personagem_teste = {"mp_atual": 50}
        consumir_mana(personagem=personagem_teste, custo_mp=20)
        
        self.assertEqual(personagem_teste["mp_atual"], 30)

    def test_consumir_mana_insuficiente(self):
        """Garante que a função levanta um ValueError se o custo for maior que a mana atual."""
        personagem_teste = {"mp_atual": 10}
        with self.assertRaises(ValueError):
            consumir_mana(personagem=personagem_teste, custo_mp=30)

    # Testes da função calcular_dano_magico

    def test_calcular_dano_magico_normal(self):
        """Testa se o dano mágico é subtraído corretamente pela resistência."""
        dano = calcular_dano_magico(poder_magico=40, resistencia_magica=15)
        self.assertEqual(dano, 25)

    def test_calcular_dano_magico_bloqueio_total(self):
        """Garante que o dano não fica negativo se a resistência for maior que o poder."""
        dano = calcular_dano_magico(poder_magico=20, resistencia_magica=50)
        self.assertEqual(dano, 0)

    def test_calcular_dano_magico_valores_negativos(self):
        """Verifica se a função bloqueia a injeção de valores negativos de poder ou resistência."""
        with self.assertRaises(ValueError):
            calcular_dano_magico(poder_magico=-10, resistencia_magica=5)
            
        with self.assertRaises(ValueError):
            calcular_dano_magico(poder_magico=30, resistencia_magica=-5)

    # Testes da função recuperar_mana

    def test_recuperar_mana_sucesso(self):
        """Testa se a mana é recuperada corretamente sem passar do limite."""
        personagem_teste = {"mp_atual": 10, "mp_maximo": 50}
        recuperar_mana(personagem=personagem_teste, quantidade=20)
        
        self.assertEqual(personagem_teste["mp_atual"], 30)

    def test_recuperar_mana_trava_no_maximo(self):
        """Garante que a recuperação de mana não ultrapassa o limite máximo (mp_maximo)."""
        personagem_teste = {"mp_atual": 40, "mp_maximo": 50}
        recuperar_mana(personagem=personagem_teste, quantidade=30) # Passaria para 70
        
        self.assertEqual(personagem_teste["mp_atual"], 50)

if __name__ == '__main__':
    unittest.main()