arq = open("hdi.csv","r")
texto = arq.readlines()
arq.close()
cont = 3
for indice in range(1,len(texto)):
    if " " in texto[indice][0:cont]:
        texto[indice] = texto[indice][cont:]
    if indice > 9 and indice < 99:
        cont = 4
    if indice > 99 and indice < 999:
        cont = 5
    if indice > 999 and indice < 9999:
        cont = 6

arq = open("new_hdi.csv","w")
arq.writelines(texto)
arq.close()
