import pandas as pd
from collections import Counter
import re

def remover_palavras(texto, palavras_remover):
  """
  Remove palavras indesejadas de uma string.

  Argumentos:
    texto: A string original.
    palavras_remover: Uma lista de palavras que devem ser removidas.

  Retorno:
    Uma string com as palavras indesejadas removidas.
  """

  # Dividir o texto em tokens
  tokens = texto.split()

  # Criar um conjunto de palavras a serem removidas
  palavras_remover = set(palavras_remover)

  # Filtrar os tokens que não estão no conjunto de palavras a serem removidas
  tokens_filtrados = [token for token in tokens if token not in palavras_remover]

  # Retornar a string com as palavras indesejadas removidas
  return ' '.join(tokens_filtrados)

palavras_remover = ["a", "o", "as", "os", "de", "do", "da", "dos", "das", "em", "no", "na", "nos", "nas", "com", "para", "por", "e", "ou", "se", "que", "mas", "como", "um", "uma", "uns", "umas", "seu", "sua", "seus", "suas", "me", "te", "lhe", "lhes", "se", "si", "lhe", "lhes"]

def obter_expressoes_uma_palavra(texto):
    # Dividir o texto em tokens considerando apenas palavras alfanuméricas e traços
    tokens = re.findall(r'\b[a-zA-Z0-9-]+\b', texto.lower())
    
    # Criar uma lista de expressões de 3 tokens
    expressoes_tres_tokens = [' '.join(tokens[i:i+1]) for i in range(len(tokens) - 1)]
    
    # Contar a frequência das expressões
    contagem_expressoes = Counter(expressoes_tres_tokens)
    
    # Retornar as 3 expressões mais comuns
    return contagem_expressoes.most_common(40)

def obter_expressoes_duas_palavras(texto):
    # Dividir o texto em tokens considerando apenas palavras alfanuméricas e traços
    tokens = re.findall(r'\b[a-zA-Z0-9-]+\b', texto.lower())
    
    # Criar uma lista de expressões de 3 tokens
    expressoes_tres_tokens = [' '.join(tokens[i:i+2]) for i in range(len(tokens) - 1)]
    
    # Contar a frequência das expressões
    contagem_expressoes = Counter(expressoes_tres_tokens)
    
    # Retornar as 3 expressões mais comuns
    return contagem_expressoes.most_common(40)

def obter_expressoes_tres_palavras(texto):
    # Dividir o texto em tokens considerando apenas palavras alfanuméricas e traços
    tokens = re.findall(r'\b[a-zA-Z0-9-/:%]+\b', texto.lower())
    
    # Criar uma lista de expressões de 3 tokens
    expressoes_tres_tokens = [' '.join(tokens[i:i+3]) for i in range(len(tokens) - 1)]
    
    # Contar a frequência das expressões
    contagem_expressoes = Counter(expressoes_tres_tokens)
    
    # Retornar as 3 expressões mais comuns
    return contagem_expressoes.most_common(40)

def obter_expressoes_quatro_palavras(texto):
    # Dividir o texto em tokens considerando apenas palavras alfanuméricas e traços
    tokens = re.findall(r'\b[a-zA-Z0-9-/:%]+\b', texto.lower())
    
    # Criar uma lista de expressões de 3 tokens
    expressoes_tres_tokens = [' '.join(tokens[i:i+4]) for i in range(len(tokens) - 1)]
    
    # Contar a frequência das expressões
    contagem_expressoes = Counter(expressoes_tres_tokens)
    
    # Retornar as 3 expressões mais comuns
    return contagem_expressoes.most_common(40)

# Carregar o arquivo Excel
caminho_arquivo = input("insira o nome do arquivo: ")  # Substitua pelo caminho do seu arquivo
nome_planilha = "Sheet1"
nome_coluna = "texto"

# Carregar a coluna do arquivo Excel
dados = pd.read_excel(caminho_arquivo, sheet_name=nome_planilha)
coluna_texto = dados[nome_coluna].dropna().astype(str)

# Concatenar todos os textos da coluna em uma única string
texto_completo = ' '.join(coluna_texto)

def obter_palavras_individuais():
    texto_sem_expressao = remover_palavras(texto_completo, palavras_remover)
    resultado = obter_expressoes_uma_palavra(texto_sem_expressao)
    print(resultado)

def obter_combo_2():
    texto_sem_expressao = remover_palavras(texto_completo, palavras_remover)
    resultado = obter_expressoes_duas_palavras(texto_sem_expressao)
    print(resultado)

def obter_combo_3():
    resultado = obter_expressoes_tres_palavras(texto_completo)
    print(resultado)

def obter_combo_4():
    resultado = obter_expressoes_quatro_palavras(texto_completo)
    print(resultado)

# Chamar a função e exibir o resultado
obter_combo_4()
