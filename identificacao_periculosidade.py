import pandas as pd

def encontrar_palavras(texto, lista_palavras):
    # Transforma o texto em minúsculas para facilitar a comparação
    texto = texto.lower()
    
    # Inicializa uma lista para armazenar as palavras encontradas
    palavras_encontradas = []
    
    # Itera sobre cada palavra da lista de palavras
    for palavra in lista_palavras:
        # Verifica se a palavra está presente no texto
        if palavra.lower() in texto:
            palavras_encontradas.append(palavra)  # Adiciona a palavra encontrada à lista
    
    return palavras_encontradas

# Lista de palavras de exemplo
lista_adn = ["adicional noturno", "20%", "22:00", "5:00", "2h00", "5h00", "20 por cento", "horas noturnas"]
lista_adp = ["periculosidade", "30%", "30 por cento", "adicional periculosidade", "adicional de risco"]
lista_ats = ["5 anos", "cinco anos", "adicional tempo",
             "tempo serviço", "tempo de serviço", "adicional por tempo", "anuênio", "biênio", "triênio", "quinquênio"]
lista_sav = ["sobreaviso", "regime sobreaviso", "1/3", "33%", "um terço"]


def testar_adn():
    arquivo = "adn_cleaned.xlsx"
    df = pd.read_excel(arquivo)
    df['Classificação'] = df['texto'].apply(lambda x: encontrar_palavras(str(x), lista_adn))
    print(df['Classificação'])

def testar_adp():
    arquivo = "adp_cleaned.xlsx"
    df = pd.read_excel(arquivo)
    df['Classificação'] = df['texto'].apply(lambda x: encontrar_palavras(str(x), lista_adp))
    print(df['Classificação'])

def testar_ats():
    arquivo = "ats_cleaned.xlsx"
    df = pd.read_excel(arquivo)
    df['Classificação'] = df['texto'].apply(lambda x: encontrar_palavras(str(x), lista_ats))
    print(df['Classificação'])

def testar_sav():
    arquivo = "sav_cleaned.xlsx"
    df = pd.read_excel(arquivo)
    df['Classificação'] = df['texto'].apply(lambda x: encontrar_palavras(str(x), lista_sav))
    print(df['Classificação'])

def testar_todos_adicionais():
    arquivo = "adicionais_geral.xlsx"
    df = pd.read_excel(arquivo)
    df['Classificação-ADN'] = df['texto'].apply(lambda x: encontrar_palavras(str(x), lista_adn))
    df['Classificação-ADP'] = df['texto'].apply(lambda x: encontrar_palavras(str(x), lista_adp))
    df['Classificação-ATS'] = df['texto'].apply(lambda x: encontrar_palavras(str(x), lista_ats))
    df['Classificação-SAV'] = df['texto'].apply(lambda x: encontrar_palavras(str(x), lista_sav))
    print(df['Classificação-ADN'], df['Classificação-ADP'], df['Classificação-ATS'], df['Classificação-SAV'])

testar_todos_adicionais()