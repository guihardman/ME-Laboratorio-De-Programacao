import unittest
from modulos.combate import calcular_dano_fisico, calcular_acerto_critico, verificar_esquiva

class TestCombate(unittest.TestCase):

    
    def test_dano_fisico_calculo_correto(self):
        self.assertEqual(calcular_dano_fisico(50, 20), 30)

    def test_dano_fisico_nao_cura_inimigo(self):
       
        self.assertEqual(calcular_dano_fisico(10, 50), 0)

    def test_dano_fisico_erro_negativo(self):
        with self.assertRaises(ValueError):
            calcular_dano_fisico(-5, 10)

   
    def test_critico_sucesso(self):
        
        self.assertEqual(calcular_acerto_critico(50, 20, 10), 100)

    def test_critico_falha(self):
        
        self.assertEqual(calcular_acerto_critico(50, 20, 50), 50)

    
    def test_esquiva_sucesso(self):
        
        self.assertTrue(verificar_esquiva(10, 15))

    def test_esquiva_falha(self):
        
        self.assertFalse(verificar_esquiva(10, 50))

if __name__ == '__main__':
    unittest.main()