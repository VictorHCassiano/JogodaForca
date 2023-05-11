import random as rd
respostas = ["victor","gustavo","magnum","lucas","felipe"]
resp = respostas[rd.randint(0,4)]
tentativa = []
print("Bem vindo ao jogo da forca ")
print(resp)
for x in resp:
    tentativa.append("_")
check = 0
chances = 0

while True:
    if chances == 10:
        print("Voce perdeu")
        break

    print(f"Voce tem {10-chances} chances")
    print(tentativa)
    letraAdivinhada = input("Digite sua tentativa:")

    for x in range(len(resp)):
        if letraAdivinhada == resp[x]:
            tentativa[x]= letraAdivinhada 
    for y in tentativa:
        
        if y == "_":
            check+=1
       
    if check == 0:
        print(f"Voce venceu!!!\na resposta era {resp}")
        exit()
    check = 0
    chances+=1
        
       
        
    
