from Semana12.Figura import Figura
from Semana12.Cuadrado import Cuadrado
from Semana12.Triangulo import Triangulo

figura = Figura(12)

print(figura)

cuadrado = Cuadrado('mediano', 'rojo', 5)

print(cuadrado.area())

triangulo = Triangulo('grande', 'azul', 2, 3, 4)
print(triangulo)