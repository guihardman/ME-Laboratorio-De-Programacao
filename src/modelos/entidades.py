"""
Módulo: entidades.py
Descrição: Contém as classes base para os personagens do jogador e inimigos.
Aplica conceitos de Herança e Encapsulamento da Programação Orientada a Objetos (POO).
"""

class Entidade:
    """
    Classe base (Mãe) que representa qualquer ser vivo no combate.
    """
    def __init__(self, nome, hp_max, mp_max, forca, inteligencia, defesa, agilidade):
        self.nome = nome
        
        # Atributos de Vida e Mana
        self.hp_max = hp_max
        self.hp_atual = hp_max
        self.mp_max = mp_max
        self.mp_atual = mp_max
        
        # Atributos de Combate
        self.forca = forca                  # Usado para ataques físicos
        self.inteligencia = inteligencia    # Usado para magias
        self.agilidade = agilidade          # Usado para definir a Iniciativa no combate
        
        # Sistema de Defesa
        self.defesa_base = defesa           # Guarda o valor original
        self.defesa_atual = defesa          # Valor que pode ser alterado durante o combate
        self.esta_defendendo = False        # Flag para a ação "Defender"
        
        # Listas para armazenar as habilidades (serão preenchidas com dados de habilidades.py)
        # Ataques devem conter: nome, poder, chance_acerto, chance_critico
        self.ataques = [] 
        # Magias devem conter: nome, elemento, poder, custo_mp
        self.magias = []  

    def receber_dano(self, quantidade_dano):
        """Reduz o HP atual, garantindo que não fique negativo."""
        self.hp_atual -= quantidade_dano
        if self.hp_atual < 0:
            self.hp_atual = 0

    def curar_hp(self, quantidade_cura):
        """Restaura o HP atual, respeitando o limite máximo."""
        self.hp_atual += quantidade_cura
        if self.hp_atual > self.hp_max:
            self.hp_atual = self.hp_max

    def gastar_mp(self, custo):
        """Deduz o MP ao usar magia. Retorna True se tiver MP suficiente, False caso contrário."""
        if self.mp_atual >= custo:
            self.mp_atual -= custo
            return True
        return False

    def esta_vivo(self):
        """Retorna True se a entidade ainda tem HP, facilitando a checagem no loop de combate."""
        return self.hp_atual > 0

    def acao_defender(self):
        """Ativa o modo de defesa para a rodada atual, aumentando a defesa."""
        self.esta_defendendo = True
        # Exemplo: Defender dobra a defesa temporariamente
        self.defesa_atual = self.defesa_base * 2 

    def resetar_defesa(self):
        """Deve ser chamado no início de cada rodada para remover o buff de defesa."""
        self.esta_defendendo = False
        self.defesa_atual = self.defesa_base


class Personagem(Entidade):
    """
    Classe Filha que representa os membros da Party controlados pelo jogador.
    Herda todos os atributos e métodos de Entidade.
    """
    def __init__(self, nome, hp_max, mp_max, forca, inteligencia, defesa, agilidade):
        # A função super() chama o construtor da classe Mãe (Entidade)
        super().__init__(nome, hp_max, mp_max, forca, inteligencia, defesa, agilidade)
        
        # Espaço para atributos exclusivos do jogador, se houver no futuro
        # Ex: self.exp_atual = 0


class Inimigo(Entidade):
    """
    Classe Filha que representa os inimigos controlados pela máquina.
    Possui o atributo adicional de 'fraqueza' elementar.
    """
    def __init__(self, nome, hp_max, mp_max, forca, inteligencia, defesa, agilidade, fraqueza_elemento):
        # Chama o construtor da classe Mãe
        super().__init__(nome, hp_max, mp_max, forca, inteligencia, defesa, agilidade)
        
        # Atributo exclusivo dos inimigos
        self.fraqueza = fraqueza_elemento  # Ex: "fogo", "gelo", "raio"