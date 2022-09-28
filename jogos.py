import forca
import adivinhacao

def apresentacao():
    print("*" * 25)
    print("\033[32;1;4mBem vindo ao Polvo Games!\033[m")
    print("*" * 25)
    escolhe_jogo()

def escolhe_jogo():
    while True:
        try:
            opcao = int(input("\nEscolha o seu jogo:\n[1]Adivinhação [2]Forca\n"))

        except:
            print("\nEscreva um número inteiro!\n")
            continue

        if opcao == 1:
            print("\n")
            print("*" * 24)
            print("Vamos jogar adivinhação!\n")
            adivinhacao.jogar()
            break

        elif opcao == 2:
            print("*" * 10)
            print("Vamos jogar forca!")
            forca.jogar()
            break

if __name__ == "__main__":
    apresentacao()