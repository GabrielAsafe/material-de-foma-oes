import hashlib

from difflib import get_close_matches



def inicializar(dictionaryFile):
    arquivo_palavras = dictionaryFile
    dicionario_hashes = criar_dicionario_hashes(arquivo_palavras)
    return dicionario_hashes

def criar_dicionario_hashes(nome_arquivo):
    dicionario_hashes = {}

    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for palavra in arquivo:
            palavra = palavra.strip()
            hash_palavra = hashlib.sha256(palavra.encode()).hexdigest()
            dicionario_hashes[hash_palavra] = palavra

    return dicionario_hashes

def sugestoes_palavras(palavra, dicionario_hashes):
    palavras_conhecidas = list(dicionario_hashes.values())
    sugestoes = get_close_matches(palavra, palavras_conhecidas, n=7, cutoff=0.8)
    return sugestoes

def verifica_palavras_corretas(palavra, dicionario_hashes):

    hash_palavra = hashlib.sha256(palavra.encode()).hexdigest()

    if hash_palavra in dicionario_hashes:
        print(f'A palavra "{palavra}" está correta.')
    else:
        sugestoes = sugestoes_palavras(palavra, dicionario_hashes)
        if sugestoes:
            print(f'A palavra "{palavra}" está incorreta. Sugestões: {", ".join(sugestoes)}')
            return ", ".join(sugestoes)
        else:
            print(f'A palavra "{palavra}" está incorreta. Nenhuma sugestão encontrada.')


