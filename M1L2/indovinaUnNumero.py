import random

secret = random.randint(1, 20)  # Generare un numero casuale da 1 a 20
tries = 5

for i in range(tries):
    guess = int(input("Tentativo " + str(i + 1) + ": Indovina il numero da 1 a 20: "))
    if guess == secret:
        print("Hai indovinato! Vittoria!")
        break
    elif guess < secret:
        print("Il numero segreto è maggiore.")
    else:
        print("Il numero segreto è minore.")
else:
    print("Non ci sono più tentativi disponibili. Il numero segreto era ", secret)