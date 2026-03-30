import unittest

# Importar funções
from modulos.inventario import adicionar_item, remover_item, usar_pocao_cura


class TestInventario(unittest.TestCase):

    #"teste de adicionar item"
    def test_adicionar_item(self):
        mochila = []
        adicionar_item(mochila, "Pocao de Vida")
        self.assertIn("Pocao de Vida", mochila)

    #"teste de remover item"
    def test_remover_item_com_sucesso(self):
        mochila = ["Espada", "Escudo"]
        remover_item(mochila, "Espada")
        self.assertNotIn("Espada", mochila)

    def test_remover_item_inexistente_gera_erro(self):
        mochila = ["Mapa"]
        with self.assertRaises(ValueError):
            remover_item(mochila, "Chave")

    #"testes de cura"
    def test_curar_personagem_normal(self):
        heroi = {'hp_atual': 50, 'hp_maximo': 100}
        usar_pocao_cura(heroi, 30)
        self.assertEqual(heroi['hp_atual'], 80)

    def test_curar_personagem_passando_do_limite(self):
        heroi = {'hp_atual': 90, 'hp_maximo': 100}
        usar_pocao_cura(heroi, 50)
        self.assertEqual(heroi['hp_atual'], 100)

    def test_curar_personagem_morto_gera_erro(self):
        heroi = {'hp_atual': 0, 'hp_maximo': 100}
        with self.assertRaises(ValueError):
            usar_pocao_cura(heroi, 50)


if __name__ == '__main__':
    unittest.main()