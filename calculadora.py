print("                   Calculadora                        ")

class Operaciones:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def suma(self):
        return self.num1 + self.num2
    def resta(self):
        return self.num1 + self.num2
    def divicion(self):
        return self.num1 + self.num2
    def multiplicacion(self):
        return self.num1 + self.num2

obj = Operaciones(10, 4)

print(obj.suma())