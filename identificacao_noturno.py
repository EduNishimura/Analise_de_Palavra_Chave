import pandas as pd

def encontrar_palavras(texto, lista_palavras):
    # Transforma o texto em minúsculas para facilitar a comparação
    texto = texto.lower()
    
    # Itera sobre cada palavra da lista de palavras
    for palavra in lista_palavras:
        # Verifica se a palavra está presente no texto
        if palavra.lower() in texto:
            return 1  # Retorna 1 assim que encontrar qualquer palavra da lista
    
    # Se nenhuma palavra for encontrada, retorna 0
    return 0

# Lista de palavras de exemplo
lista_palavras = ["adicional noturno", "20%", "22:00", "5:00", "2h00", "5h00", "noturno", "20 por cento"]

arquivo = "adn_cleaned.xlsx"
df = pd.read_excel(arquivo)
df['Classificação'] = df['texto'].apply(lambda x: encontrar_palavras(str(x), lista_palavras))
print(df['Classificação'])