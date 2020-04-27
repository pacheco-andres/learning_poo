print("-------------AREA DE UN CUADRADO--------------")
print("")
print("~" * 70)

print("")
class Cuadrado:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def area(self):
        resultado = self.num1 * self.num2
        if self.num1 == self.num2:
            print("El area del cuadarado es: ", resultado)
        else:
            print("no se puede obtener el arae, ya que los datos deben ser iguales")
    
final = Cuadrado(10, 10)    

final.area()

