import os

#Funcions lambda
suma = lambda x,y: x + y
resta = lambda x,y: x - y
multiplicar = lambda x,y: x * y
dividir = lambda x,y: x / y



ruta_base = os.path.dirname(__file__)
ruta_a_recurs = os.path.join(ruta_base, "fitxer.txt")
f = open(ruta_a_recurs)#Obri l'arxiu en modo lectura

for linia in f:#Inicia bucle for per a recorrer l'arxiu                              
    llista = linia.split()#Creem una llista de cada valor de la linia
    if llista[1] == "+":
        num1 = int(llista[0])
        num2 = int(llista[2])
        resultat = suma(num1, num2)
        print(str(num1) + "+" + str(num2) + "=" + str(resultat))

    if llista[1] == "-":
        num1 = int(llista[0])
        num2 = int(llista[2])
        resultat = resta(num1, num2)
        print(str(num1) + "-" + str(num2) + "=" + str(resultat))
    
    if llista[1] == "*":
        num1 = int(llista[0])
        num2 = int(llista[2])
        resultat = multiplicar(num1, num2)
        print(str(num1) + "-" + str(num2) + "=" + str(resultat))
    
    if llista[1] == "/":
        num1 = int(llista[0])
        num2 = int(llista[2])
        resultat = dividir(num1, num2)
        print(str(num1) + "-" + str(num2) + "=" + str(resultat))
f.close() #Tanca l'arxiu

