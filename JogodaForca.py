import random as rd

palavras = ["victor", "gustavo", "magnum", "lucas", "felipe"]
palavra_secreta = palavras[rd.randint(0, 4)]
letras_adivinhadas = []
chances = 0
for x in palavra_secreta:
    letras_adivinhadas.append("_")
print("Bem vindo ao jogo da forca")
print(palavra_secreta)

while True:
    if chances == 10:
        print("Voce perdeu")
        exit()

    print(f"Voce tem {10 - chances} chances")
    print(" ".join(letras_adivinhadas))
    
    letra_adivinhada = input("Digite uma letra: ")
    if len(letra_adivinhada) != 1:
        print("Por favor, digite apenas uma letra.")
        continue
    
    acertou = False
    for i, letra in enumerate(palavra_secreta):
        if letra == letra_adivinhada:
            letras_adivinhadas[i] = letra
            acertou = True
    
    if not acertou:
        chances += 1

    if "_" not in letras_adivinhadas:
        print(f"Voce venceu!!!\na resposta era {palavra_secreta}")
        exit()
