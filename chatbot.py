#Le preguntamos al usuario su nombre
name = input("¿Como te llamas? ")
#preguntamos d´ónde vive
texto_interpolado = f"Hola {name}, un gusto, ¿Dónde vives? "
ciudad = input(texto_interpolado)
#usando el nombre que nos ha dicho le preguntamos su comida favorita de la ciudad
comida = input(f"¿Cuál es tu comida favorita {name}? ")
#le damos una respuesta a la comida que nos ha dicho
gusto = input(f"Con que tu comida favorita es {comida}, la típica")
#le preguntamos que día nació
edad = input("¿Qué día naciste? ")
#convertimos el input a un float
try:
    float_number = float(edad)
    print("Input as float: ", float_number)
except ValueError:
    print("Invalid Input. Please enter a valid number from 1 to 31")
