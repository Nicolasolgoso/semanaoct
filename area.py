#aquí calculamos el área
def area_triangulo(altura,base):
    area = altura * base / 2
    return area
#le pedimos al usuario la altura y la base del triángulo
altura_input = float(input("Altura?: "))
base_input = float(input("Base?: "))
#le deveolvemos el área calculada
area_calculada = area_triangulo(base_input,altura_input)
print(area_calculada)
