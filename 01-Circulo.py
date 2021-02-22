from circulo import Circulo

radio = float(input("Ingrese el radio de un circulo: "))
circulo = Circulo(radio)

print("El Diámetro es:", round(circulo.diametro(),2))
print("El Perímetro es:",round(circulo.perimetro(),2))
print("El Área es:",round(circulo.area(),2))