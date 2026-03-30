import unittest
from modulos.entidades import criar_personagem, aplicar_dano, esta_vivo

class TestEntidades(unittest.TestCase):

    def test_criar_personagem_caminho_feliz(self):
        # Cria um personagem válido
        heroi = criar_personagem(nome="Arthur", hp_maximo=100, ataque=20, defesa=10)
        
        # Verifica se o dicionário foi montado corretamente
        self.assertEqual(heroi["nome"], "Arthur")
        self.assertEqual(heroi["hp_atual"], 100) # hp_atual tem que começar cheio

    def test_criar_personagem_hp_zero_ou_negativo(self):
        # assertRaises verifica se a função da ValueError quando passamos vida -50
        with self.assertRaises(ValueError):
            criar_personagem(nome="Fantasma", hp_maximo=-50, ataque=10, defesa=5)

    def test_aplicar_dano_normal(self):
        monstro = {"nome": "Monstro", "hp_atual": 50}

        aplicar_dano(monstro, 20)
  
        self.assertEqual(monstro["hp_atual"], 30)

    def test_aplicar_dano_fatal_trava_no_zero(self):
        monstro = {"nome": "Monstro", "hp_atual": 10}
        
        aplicar_dano(monstro, 999)
        
        self.assertEqual(monstro["hp_atual"], 0)

    def test_esta_vivo_verdadeiro(self):
        heroi = {"hp_atual": 1} 
        self.assertTrue(esta_vivo(heroi)) # Tem que dar True

    def test_esta_vivo_falso(self):
        heroi = {"hp_atual": 0} # Morreu
        self.assertFalse(esta_vivo(heroi)) # Tem que dar False

if __name__ == '__main__':
    unittest.main()