def investimentos():
    p1 = input("Você estuda? (responda com 'S' para sim e 'N' para não): ").upper()
    while p1 not in ['S', 'N']:
        p1 = input("Resposta inválida. Por favor, responda com 'S' ou 'N': ").upper()
    p2 = input("você investe? (responda com 'S' para sim e 'N' para não): ").upper()
    while p2 not in ['S', 'N']:
        p2 = input("Resposta inválida. Por favor, responda com 'S' ou 'N': ").upper()
    p3 = int(input("Caso invista, investe quanto por mês?"))
    p4 = int(input("Qual sua renda mensal?:"))
    p5 = input("Você conhece nossos serviços? (responda com 'S' para sim e 'N' para não): ").upper()
    while p5 not in ['S', 'N']:
        p5 = input("Resposta inválida. Por favor, responda com 'S' ou 'N': ").upper()
    
    
    if p1 == "S" and p2 =="S" and p5 =="S":
        print("Podemos ajuda-lo nessa etapa")
        
    if p3 <=3000 and p4 <= 3000:
        print("podemos aumentar a sua renda com investimentos certos")
    else:
        print("Já pensou em ir pra criptomoeda?")
    
    
    if p1 =="N" or p2 =="N" or p5 == "N":
        print("ENTÃO TIRA A BUNDA DA CAMA E VAI ESTUDAR")
    input("\npressione enter para sair...")
    return

investimentos()