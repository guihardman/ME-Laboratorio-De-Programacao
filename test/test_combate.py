import unittest

from modulos.combate import calcular_dano_fisico, calcular_acerto_critico, verificar_esquiva

class TestCombate(unittest.TestCase):

    # Testes da função calcular_dano_fisico

    def test_calcular_dano_fisico_positivo(self):
        """Testa o caminho feliz onde o ataque supera a defesa."""
        resultado = calcular_dano_fisico(ataque=30, defesa=10)
        self.assertEqual(resultado, 20)

    def test_calcular_dano_fisico_defesa_maior_que_ataque(self):
        """Garante que o dano não fique negativo se a armadura for muito forte (retorna 0)."""
        resultado = calcular_dano_fisico(ataque=15, defesa=30)
        self.assertEqual(resultado, 0)

    def test_calcular_dano_fisico_valores_negativos(self):
        """Verifica se o erro correto (ValueError) é levantado ao passar números negativos."""
        with self.assertRaises(ValueError):
            calcular_dano_fisico(ataque=-10, defesa=5)

    # Testes da função calcular_acerto_critico

    def test_calcular_acerto_critico_sucesso(self):
        """Testa o cenário onde a rolagem é menor que a chance, causando dano duplo."""
        # Dano 15, Chance 30%, Tirou 20 no dado. 20 <= 30, então deve dobrar (30).
        resultado = calcular_acerto_critico(dano_base=15, chance_critico=30, rolagem_dado=20)
        self.assertEqual(resultado, 30)

    def test_calcular_acerto_critico_falha(self):
        """Testa o cenário onde o dado rolou alto e não deu crítico, mantendo o dano base."""
        # Dano 15, Chance 30%, Tirou 80 no dado. Não dobra.
        resultado = calcular_acerto_critico(dano_base=15, chance_critico=30, rolagem_dado=80)
        self.assertEqual(resultado, 15)

    def test_calcular_acerto_critico_erro_negativo(self):
        """Garante que a função levanta ValueError se o dano base for negativo."""
        with self.assertRaises(ValueError):
            calcular_acerto_critico(dano_base=-5, chance_critico=20, rolagem_dado=10)

    # Testes da função verificar_esquiva

    def test_verificar_esquiva_sucesso(self):
        """Testa quando a rolagem do dado está dentro da porcentagem de esquiva."""
        # Agilidade 20 = 40% de chance. Tirou 30 no dado. Deve retornar True.
        resultado = verificar_esquiva(agilidade_defensor=20, rolagem_dado=30)
        self.assertTrue(resultado)

    def test_verificar_esquiva_falha(self):
        """Testa quando o dado rola um valor acima da chance de esquiva."""
        # Agilidade 20 = 40% de chance. Tirou 60 no dado. Deve retornar False.
        resultado = verificar_esquiva(agilidade_defensor=20, rolagem_dado=60)
        self.assertFalse(resultado)

    def test_verificar_esquiva_trava_limite_maximo(self):
        """Garante que a esquiva nunca ultrapassa o limite de 80%, mesmo com agilidade absurda."""
        # Agilidade 100 daria 200%, mas a função tem um limite de 80 (min(agilidade * 2, 80)).
        # Rolando um 90 no dado, o golpe tem que acertar (retornar False para a esquiva).
        resultado = verificar_esquiva(agilidade_defensor=100, rolagem_dado=90)
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()