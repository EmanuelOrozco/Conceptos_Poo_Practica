#Un atributo de clase afecta a todos los objetos de esa clase. Es decir,
#si algun objeto cambia el valor de este atributo, este cambiara para todas las clases
# el atributo es __class__

class Circulo:

    contador: int = 0

    def __init__(self):
        self.radio = 0
        self.__class__.contador += 1


c1 = Circulo()
print(c1.contador)
c2 = Circulo()
c3 = Circulo()
c4 = Circulo()
print(c1.contador)
