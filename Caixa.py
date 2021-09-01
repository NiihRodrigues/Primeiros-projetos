print("Seja bem vindx")

valorU = float(input("Insira o valor unitário: "))
quantidade = int(input("Insira a quantidade de itens: "))
valorP = valorU * quantidade
print("Valor a pagar: ", valorP, sep="R$")

valorE = float(input("Insira o valor pago: "))
troco = valorE - valorP
print("O troco é de: ", troco, sep="R$")
print("Obrigado pela preferência<3")
