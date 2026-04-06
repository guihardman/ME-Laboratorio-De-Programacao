class NPC:
    def __init__(self, nome, personalidade, historia):
        self.nome = nome
        self.personalidade = personalidade
        self.historia = historia
        self.memoria = []

    def lembrar(self, texto):
        self.memoria.append(texto)

    def contexto(self):
        return "\n".join(self.memoria[-5:])