from math import pi

class Circulo:
    def __init__(self,radio):
        self.radio = radio
        print("Objeto circulo creado, con radio:", self.radio)
    
    def diametro (self):
        return self.radio * 2

    def perimetro (self):
     return 2 * pi * self.radio

    def area (self):
        return pi * (self.radio ** 2)