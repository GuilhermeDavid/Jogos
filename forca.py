import random

def jogar():

    palavras = lerArquivo()
    # Sorteia qual será a palavra secreta
    palavraSecreta = palavras[random.randrange(0, len(palavras))]

    # Monta uma lista escondendo as letras da palavra secreta
    letrasAcertadas = ["_" for letra in palavraSecreta]
    enforcou = False
    acertou = False
    erros = 0

    print(letrasAcertadas)
    while (not enforcou and not acertou):
        chute = input("Digite uma letra: ")
        
        #Verifica se foi digitado apenas uma letra.
        while (len(chute) > 1):
            chute = input("Por favor, digite apenas uma letra: ")
            
        # Função strip tira os espaços entre a string.
        chute = chute.strip().upper()
        index = 0

        if (chute in palavraSecreta):
            for letra in palavraSecreta:
                if (chute.upper() == letra.upper()):
                    letrasAcertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Falta(m) {} tentativa(s).".format(6-erros))

        enforcou = erros == 6
        acertou = "_" not in letrasAcertadas

        print(letrasAcertadas)

    if (acertou):
        print("Você ganhou")
    else:
        print("Você perdeu")


def lerArquivo():
    #Open("Nome do arquivo", "Tipo de paramentro, sendo r = read, w = write, a = add")
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
       # A lista palavras guardará todas as palavras possíveis sem o \n e em uppercase.
        palavras.append(linha.strip().upper())

    arquivo.close()
    return palavras

if (__name__ == "__main__"):
    jogar()
