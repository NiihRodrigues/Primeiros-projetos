fem = "vinda!"
masc = "vindo!"

gen = int(input("Qual seu pronome? \n"
                "1- Ela/Dela \n"
                "2- Ele/ Dele \n"
                "Eu escolho: "))

if gen == 1:
    print("\nSeja bem {}".format(fem))

if gen == 2:
    print("\nSeja bem {}".format(masc))

else:
    print("\nVocê só pode escolher 1 ou 2")
