print("Seja bem vindx")

valorU = float(input("\nInsira o valor unitário: "))
quantidade = int(input("Insira a quantidade de itens: "))
valorP = valorU * quantidade
print("Valor a pagar: R$%.2f" % valorP)

valorE = float(input("\nInsira o valor pago: "))
troco = valorE - valorP
print("O troco é de: R$%.2f" % troco)
print("\nObrigado pela preferência<3")
