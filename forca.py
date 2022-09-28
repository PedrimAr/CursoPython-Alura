from random import randint

def jogar():
    apresentacao()
    menu()

def apresentacao():
    print("*" * 27)
    print("\033[32;1;4mBem vindo ao jogo da forca!\033[m")
    print("*" * 27)

def menu():
    palavras = []

    while True:
        secreta = ''
        try:
            nivel = int(input("\nEscolha o nível de dificuldade:\n[1]Fácil [2]Médio [3]Difícil [4]Impossível: "))
        except:
            print("\nEscreva um número inteiro!\n")
            continue

        i = 0

        if nivel == 1:
            arquivo = open("facil.txt", "r", encoding="utf-8")
            break

        elif nivel == 2:
            arquivo = open("medio.txt", "r", encoding="utf-8")
            break

        elif nivel == 3:
            arquivo = open("dificil.txt", "r", encoding="utf-8")
            break

        elif nivel == 4:
            arquivo = open("impossivel.txt", "r", encoding="utf-8")
            break

    sorteia_secreta(arquivo, palavras, secreta)

def sorteia_secreta(arquivo, palavras, secreta):
    tentativas = 0
    i = 0

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    num = randint(0, len(palavras) - 1)
    secreta = palavras[num]

    for letra in secreta:
        i += 1

    tentativas = i + 1

    chutes(secreta, tentativas)

def define_parcial(secreta):
    parcial = []
    for letra in secreta:
        parcial += ['_']
    return parcial


def chutes(secreta, tentativas):
    parcial = define_parcial(secreta)
    printa_parcial(secreta)

    while tentativas > 0:
        index = 0
        chute = str(input("\nChute uma letra: ")).strip()
        tentativas -= 1

        if chute.lower() == secreta.lower():
            print("\n")
            print("*" * 30)
            print(f"Parabéns, você ganhou!\nA palavra era {secreta}.")
            break

        else:
            for letra in secreta:
                if (chute.lower() == letra.lower()):
                    parcial[index] = chute
                index += 1

        for l in parcial:
            print(l, end="")

        if (parcial.count("_") == 0):
            print("\n")
            print("*" * 30)
            print(f"Parabéns, você ganhou!\nA palavra era {secreta}.")
            break

    perdeu(secreta, tentativas)

def printa_parcial(secreta):
    parcial = define_parcial(secreta)

    print("\n")
    for l in parcial:
        print(l, end="")

def perdeu(secreta, tentativas):
    if tentativas == 0:
        print("\n")
        print("*" * 30)
        print(f"Você perdeu, tente novamente!\nA palavra era {secreta}.")

if __name__ == "__main__":
    jogar()