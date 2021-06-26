import math

class Punto:
    def __init__(self, X=0, Y=0):
        self.X = X
        self.Y = Y

    def __str__(self):
        return(f"({self.X},{self.Y})")

    def cuadrante(self):
        if self.X == 0 and self.Y == 0:
            print(f"El punto esta sobre el origen.")
        elif self.X > 0 and self.Y > 0:
            print(f"El punto se encuentra en el primer cuadrante.")
        elif self.X < 0 and self.Y > 0:
            print(f"El punto esta en el segundo cuadrante")
        elif self.X < 0 and self.Y < 0:
            print(f"El punto se encuentra en el tercer cuadrante")
        elif self.X > 0 and self.Y < 0:
            print(f"El punto se encuentra en el cuarto cuadrante.")
        elif self.X != 0 and self.Y == 0:
            print(f"El punto esta sobre el eje X")
        else:
            print(f"El punto esta sobre el eje Y")

    def vector(self, p):
        resultado_x = self.X - p.X 
        resultado_y = + self.Y - p.Y
        return (f"El vector entre ambos puntos es {resultado_x} y {resultado_y}")

    def distancia(self, p):
        primer_resultado = pow((p.X - self.X) + (p.Y - self.Y),2)
        segundo_resultado = math.sqrt(primer_resultado)
        return (f"La distancia entre los puntos es {segundo_resultado:.2f}")
        

class Rectangulo:
    def __init__(self, p_inicial = Punto(), p_final = Punto()):
        self.p_inicial = p_inicial
        self.p_final = p_final

        self.altura = abs(self.p_inicial.Y - self.p_final.Y)
        self.base = abs(self.p_inicial.X - self.p_final.X)
        self.area = abs(self.base * self.altura)

    def alturaf(self):
        return(f"La altura del rectángulo es {self.altura}")

    def basef(self):
        return(f"La base del rectángulo es {self.base}")

    def areaf(self):
        return(f"El area del rectángulo es {self.area}")


#Pruebas

A = Punto(2,3)
B = Punto(5,5) 
C = Punto(-3,-1) 
D = Punto(0,0)

print(A)
print(B)
print(C)
print(D)

A.cuadrante()
C.cuadrante()
D.cuadrante()

print(A.vector(B))
print(B.vector(A))

print(A.distancia(B))
print(B.distancia(A))

print(A.distancia(D))
print(B.distancia(D))
print(C.distancia(D))

E = Rectangulo(A,B)

print(E.basef())
print(E.alturaf())
print(E.areaf())
