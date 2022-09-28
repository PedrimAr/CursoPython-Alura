from random import randint

def jogar():
    print("*" * 35)
    print("\033[32;1;4mBem vindo ao jogo de adivinhação!\033[m")
    print("*" * 35)
    while True:
        try:
            nivel = int(input("\nEscolha o nível de dificuldade:\n[1]Fácil [2]Médio [3]Difícil [4]Impossível\n"))
        except:
            print("\nEscreva um número inteiro!\n")
            continue

        if nivel == 1:
            total_tentativa = 10
            teto = 100
            break

        elif nivel == 2:
            total_tentativa = 5
            teto = 100
            break

        elif nivel == 3:
            total_tentativa = 3
            teto = 100
            break

        elif nivel == 4:
            total_tentativa = 3
            teto = 125
            break

        else:
            print("\nNúmero inválido!\n")

    pontos = 1000

    num_sec = randint(1, teto)

    for rodada in range(1, total_tentativa + 1):
        print("-" * 15)
        print(f"Rodada: {rodada} \n")
        
        while True:
            try:
                num_chu = int(input(f"Digite um número entre 1 a {teto}: "))
            except:
                print("\nEscreva um número inteiro!\n")
                continue
            if num_chu < 1 or num_chu > teto:
                print("\nNúmero inválido!\n")
            else:
                break


        acertou = num_chu == num_sec
        maior = num_chu > num_sec
        menor = num_chu < num_sec

        if acertou:
            print(f"Você acertou e fez {pontos} pontos!")
            break

        else:
            if maior:
                print("Você errou! O número que você chutou está acima do número secreto.")

            elif menor:
                print("Você errou! O número que você chutou está abaixo do número secreto.")

            pontos = pontos - abs(num_sec - num_chu)

    print(f"\nFim do jogo!\nO número era {num_sec}")

if __name__ == "__main__":
    jogar()
