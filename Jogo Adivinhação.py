import random

def main():
    target = random.randint(1, 20)
    total = target
    primeira_rodada = True
    
    while total <= 100:
        if primeira_rodada:
            guess = int(input("Digite seu palpite (um número de 1 a 20): "))
            if guess < 1 or guess > 20:
                print("Por favor, escolha um número entre 1 e 20 na primeira rodada.")
                continue
        else:
            guess = int(input("Digite seu palpite (um número de 1 a 100): "))
            if guess < 1 or guess > 100:
                print("Por favor, escolha um número entre 1 e 100 a partir da segunda rodada.")
                continue

        print("Alvo escolhido pelo computador:", target)
        print("Seu palpite:", guess)
        if guess == target:
            print("Parabéns! Você acertou o alvo.")
            break
        else:
            print("Você errou. Tente novamente.")
            if total + 20 > 100:
                print("O alvo ultrapassará 100. Você perdeu.")
                break
            new_number = random.randint(1, 20)
            total += new_number
            target += new_number
            primeira_rodada = False  
    else:
        print("Você ultrapassou 100. O computador venceu.")

if __name__ == "__main__":
    main()