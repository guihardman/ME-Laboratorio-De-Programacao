import google.generativeai as genai

genai.configure(api_key="AIzaSyDvoh6enWCqgPseGq6bQGDS3Hh5n6TRIe0")

modelo = genai.GenerativeModel("gemini-2.5-flash")

def conversar(npc, mensagem, party):
    nomes_party = ", ".join([heroi.nome for heroi in party])

    prompt = f"""
    Você é {npc.nome}
    Personalidade: {npc.personalidade}
    História: {npc.historia}

    Heróis presentes:
    {nomes_party}

    Memória:
    {npc.contexto()}

    Jogador: {mensagem}
    """

    resposta = modelo.generate_content(prompt)

    npc.lembrar(f"Jogador: {mensagem}")
    npc.lembrar(f"{npc.nome}: {resposta.text}")

    return resposta.text