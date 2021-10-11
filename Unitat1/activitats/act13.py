import random
import math

seguir = True
numRandom = random.randint(0, 100)

class ErrorEnterMassaMenut(Exception):
    def __init__(self, msg="Valor massa menut"):
        self.msg=msg
        super().__init__(self.msg)

class ErrorEnterMassaGran(Exception):
    def __init__(self, msg="Valor massa gran"):
        self.msg=msg
        super().__init__(self.msg)

while seguir:
    try:
        num = int(input("Digues un numero: "))
        if(math.isnan(num)):#math.isnan retorna True si el valor introduit es no numeric, nan(Not a Number)
            seguir == False
        elif(num < numRandom):
            raise ErrorEnterMassaMenut()
        elif(num > numRandom):
            raise ErrorEnterMassaGran()           
        elif(num == numRandom):
            print("Enhorabona, has encertat el numero!")
            seguir = False

    except ErrorEnterMassaGran as emg:
        print(emg.msg)
        print()
    except ErrorEnterMassaMenut as emm:
        print(emm.msg)
        print()
    #except ValueError():
    #    break

        
        