import unittest

from modulos.inventario import adicionar_item, remover_item, usar_pocao_cura

class TestInventario(unittest.TestCase):

    # Testes da função adicionar_item

    def test_adicionar_item_sucesso(self):
        """Verifica se um item é adicionado corretamente à lista de inventário."""
        mochila = ["Poção de Cura"]
        adicionar_item(inventario=mochila, item="Espada Longa")
        
        # O inventário agora deve ter 2 itens e a espada deve estar lá
        self.assertEqual(len(mochila), 2)
        self.assertIn("Espada Longa", mochila)

    # Testes da função remover_item

    def test_remover_item_sucesso(self):
        """Verifica se um item existente é removido da lista."""
        mochila = ["Poção de Cura", "Escudo"]
        remover_item(inventario=mochila, item="Poção de Cura")
        
        # O inventário deve ter 1 item e a poção não pode mais estar lá
        self.assertEqual(len(mochila), 1)
        self.assertNotIn("Poção de Cura", mochila)

    def test_remover_item_inexistente_erro(self):
        """Garante que tentar remover um item que não está na mochila levante ValueError."""
        mochila = ["Escudo"]
        with self.assertRaises(ValueError):
            remover_item(inventario=mochila, item="Cajado Mágico")

    # Testes da função usar_pocao_cura

    def test_usar_pocao_cura_sucesso(self):
        """Testa se a cura soma corretamente quando a vida está baixa."""
        personagem_teste = {"hp_atual": 30, "hp_maximo": 100}
        usar_pocao_cura(personagem=personagem_teste, valor_cura=40)
        
        self.assertEqual(personagem_teste["hp_atual"], 70)

    def test_usar_pocao_cura_trava_no_maximo(self):
        """Garante que a poção não cure além do HP máximo do personagem."""
        personagem_teste = {"hp_atual": 80, "hp_maximo": 100}
        # Curar 50 passaria de 100, mas a função deve travar em 100
        usar_pocao_cura(personagem=personagem_teste, valor_cura=50)
        
        self.assertEqual(personagem_teste["hp_atual"], 100)

    def test_usar_pocao_cura_erro_personagem_morto(self):
        """Verifica se levanta ValueError ao tentar curar alguém com 0 ou menos de HP."""
        personagem_teste = {"hp_atual": 0, "hp_maximo": 100}
        with self.assertRaises(ValueError):
            usar_pocao_cura(personagem=personagem_teste, valor_cura=50)

    def test_usar_pocao_cura_erro_vida_cheia(self):
        """Verifica se levanta ValueError ao tentar usar poção com o HP já no máximo."""
        personagem_teste = {"hp_atual": 100, "hp_maximo": 100}
        with self.assertRaises(ValueError):
            usar_pocao_cura(personagem=personagem_teste, valor_cura=20)

if __name__ == '__main__':
    unittest.main()