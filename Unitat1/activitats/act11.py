#Funcions lambda
suma = lambda x,y: x + y
resta = lambda x,y: x - y
multiplicar = lambda x,y: x * y
dividir = lambda x,y: x / y


def lletgirFitxer():
    #Obri l'arxiu en modo lectura
    f = open('fitxer.txt', 'r')
    #Inicia bucle infinit per a llegir linia a linia
    while True:
        linia = f.readline() #Llig linia
        if not linia:
            break #Si no hi ha mes linies trenca el bucle
        else:
            llista = linia.split()
            if llista[1] == "+":
                num1 = int(llista[0])
                num2 = int(llista[2])
                resultat = suma: (x: num1, y: num2, llista)
                print(num1 + "+" + num2 + "=" + resultat)

            if llista[1] == "-":
                num1 = int(llista[0])
                num2 = int(llista[2])
                resultat = resta(num1 - num2)
                print(num1 + "-" + num2 + "=" + resultat)
            
            if llista[1] == "*":
                num1 = int(llista[0])
                num2 = int(llista[2])
                resultat = multiplicar(num1 * num2)
                print(num1 + "*" + num2 + "=" + multiplicar)
            
            if llista[1] == "/":
                num1 = int(llista[0])
                num2 = int(llista[2])
                resultat = dividir(num1 / num2)
                print(num1 + "/" + num2 + "=" + dividir)
    f.close() #Tanca l'arxiu

lletgirFitxer()