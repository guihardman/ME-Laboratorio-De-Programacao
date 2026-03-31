import unittest

from modulos.dados import MAGIAS_DISPONIVEIS, CLASSES_DISPONIVEIS

class TestDados(unittest.TestCase):

    def test_estruturas_magias_disponiveis(self):
        """Verifica se todas as magias possuem os atributos corretos e tipos válidos."""
        chaves_esperadas = {"custo_mp", "poder_base", "tipo"}
        
        for magia, atributos in MAGIAS_DISPONIVEIS.items():
            # Garante que não falta nenhuma chave importante na magia
            self.assertTrue(chaves_esperadas.issubset(atributos.keys()), 
                            f"A magia '{magia}' não possui todas as chaves necessárias.")
            
            # Garante que o tipo de magia é apenas 'dano' ou 'cura'
            self.assertIn(atributos["tipo"], ["dano", "cura"], 
                          f"O tipo da magia '{magia}' é inválido.")

    def test_estruturas_classes_disponiveis(self):
        """Verifica se todas as classes possuem os status base necessários para o jogo não quebrar."""
        chaves_esperadas = {
            "hp_maximo", "mp_maximo", "ataque", "defesa",
            "poder_magico", "resistencia_magica", "velocidade", "magias"
        }
        
        for classe, atributos in CLASSES_DISPONIVEIS.items():
            # O issubset verifica se todas as chaves esperadas estão dentro do dicionário da classe
            self.assertTrue(chaves_esperadas.issubset(atributos.keys()), 
                            f"A classe '{classe}' não possui todos os atributos base.")
            
            # Verifica se os status não são negativos
            self.assertTrue(atributos["hp_maximo"] > 0, f"A classe '{classe}' tem HP inválido.")

    def test_magias_das_classes_existem(self):
        """Garante que as magias atribuídas às classes realmente existem no dicionário de magias."""
        for classe, atributos in CLASSES_DISPONIVEIS.items():
            for magia in atributos["magias"]:
                # Ex: se a classe 'guerreiro' tiver a magia 'luz divina', ela OBRIGATORIAMENTE tem de estar em MAGIAS_DISPONIVEIS
                self.assertIn(magia, MAGIAS_DISPONIVEIS, 
                              f"A magia '{magia}' da classe '{classe}' não está registada em MAGIAS_DISPONIVEIS.")

if __name__ == '__main__':
    unittest.main()