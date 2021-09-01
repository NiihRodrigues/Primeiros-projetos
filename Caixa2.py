print("Seja bem vindx")

valorU = float(input("Insira o valor unitário: "))
quantidade = int(input("Insira a quantidade de itens: "))
valorP = valorU * quantidade
print("Valor a pagar: ", valorP, sep="R$")

cont = int(input("\nDeseja continuar comprando?\n"
                 "Sim(1)\n"
                 "Não(2)\n"
                 ""))
if cont == 1:
    valorU2 = float(input("Insira o valor unitário: "))
    quantidade2 = int(input("Insira a quantidade de itens: "))
    valorP2 = valorU2 * quantidade2
    valorF = valorP + valorP2
    print("\nValor a pagar: ", valorF, sep="R$")

    valorE = float(input("Insira o valor pago: "))
    troco = valorE - valorF
    print("\nO troco é de: ", troco, sep="R$")
    print("Obrigado pela preferência<3")

else:
    valorE = float(input("Insira o valor pago: "))
    troco = valorE - valorP
    print("\nO troco é de: ", troco, sep="R$")
    print("Obrigado pela preferência<3")
