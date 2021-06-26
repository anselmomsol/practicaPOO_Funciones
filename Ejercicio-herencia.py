
class Persona:
    def __init__(self, nombre = " ", edad = 0 , DNI = " "):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

    def mostrar(self):
        return (f"La persona se llama {self.nombre}, su edad es {self.edad} y su DNI es {self.DNI}")

    def esMayorDeEdad(self):
        if self.edad >= 18:
            return True
        else: return False


class Cuenta:
    def __init__(self, titular = Persona(), cantidad = 0):
        self.titular = titular
        self.cantidad = cantidad
    
    def mostrar(self):
        titular = self.titular.nombre
        print(f"""Datos:
El titular de la cuenta es {titular}
Su saldo de la cuenta es $ {self.cantidad}""")

    def ingresar(self, cantidad):
        if cantidad > 0:
            cantidad += self.cantidad
            self.cantidad = cantidad
            print(f"La cantidad ahora es $ {cantidad}")
        else:
            print(f"La cantidad sigue siendo $ {self.cantidad}")

    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad = self.cantidad - cantidad
            print(f"El saldo de la cuenta ahora es $ {self.cantidad}")
            if self.cantidad < 0:
                print(f"La cuenta tiene saldo negativo!!!")


class Cuenta_joven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad = cantidad)
        self.bonificacion = bonificacion

    def titular_valido(self):
        if self.titular.esMayorDeEdad() and self.titular.edad <= 25:
            return True
        else:
            return False


    def retirar(self, cantidad):
        if self.titular_valido():
            return super().retirar(cantidad)
        else:
            print(f"Usted no puede retirar dinero.")

    def mostrar(self):
        titular = self.titular.nombre
        print("Cuenta Joven.")
        print(f"El titular de la cuenta es {titular}")
        print(f"Esta es una cuenta con una bonificacion del {self.bonificacion} %")

#Pruebas.

Nicolas = Persona("Nicolas", 27, 30200123)

print(Nicolas.mostrar())
print(Nicolas.esMayorDeEdad())

Cuenta_Nicolas = Cuenta(Nicolas, 5000)

Cuenta_Nicolas.mostrar()
Cuenta_Nicolas.ingresar(500)
Cuenta_Nicolas.ingresar(0)
Cuenta_Nicolas.retirar(125)

Jorge = Persona("Jorge", 19, 40200123)
Cuenta_Jorge = Cuenta_joven(Jorge, 1500, 30)

print(Cuenta_Jorge.titular_valido())
Cuenta_Jorge.retirar(400)
Cuenta_Jorge.ingresar(1000)
Cuenta_Jorge.mostrar()