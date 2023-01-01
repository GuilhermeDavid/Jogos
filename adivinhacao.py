import random

def jogar():
    numSecreto = random.randint(0, 10)
    totalTentativas = 0
    pontuacao = 0
    nivel = 0

    print("Escolha a dificuldade:")
    print("(1) Fácil, (2) Médio, (3) Difícil")
    nivel = int(input("Digite:"))
    while (nivel < 1 or nivel > 3):
        print("Número inválido:")
        print("(1) Fácil, (2) Médio, (3) Difícil")
        nivel = int(input("Digite:"))

    # Sistema de pontos que varia dependendo da dificuldade escolhida
    if (nivel == 1):
        pontuacao = 1000
        totalTentativas = 5
    elif (nivel == 2):
        pontuacao = 1500
        totalTentativas = 4
    else:
        pontuacao = 2000
        totalTentativas = 3

    for i in range(1, totalTentativas + 1):
        print("Tentativa: {} de {}".format(i, totalTentativas))
        chute = int(input("Digite um número entre 0 e 10: "))
        while (chute < 0 or chute > 10):
            chute = int(
                input("Número inválido, Digite um número entre 0 e 10: "))
        if (chute == numSecreto):
            print("Você acertou")
            print("Sua pontuação é de {} pontos".format(pontuacao))
            break
        else:
            pontuacao -= 200
            if (chute > numSecreto and i < 3):
                print("Tente um número menor")

            if (chute < numSecreto and i < 3):
                print("Tente um número maior")

    if (chute != numSecreto):
        pontuacao = 0
        print("Você perdeu o jogo, o número secreto era:", numSecreto)

if (__name__ == "__main__"):
    jogar()
