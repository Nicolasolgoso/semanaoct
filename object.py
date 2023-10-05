initial_position= float(input("Enter the initial height:"))
#He puesto esto para pedir al usuario la altura inicial
time = 5
#He cogido como valor de tiempo 5 segundos
gravity = 9.81
#Esto es la constante de gravedad
initial_velocity = float(input("Enter the initial velocity(in m/s):"))
#Aquí le pregunto al usuario la velocidad inicial
final_position  = initial_position + initial_velocity * time + 0.5 * gravity * time * time
#Esta es la fórmula utilizada para calcular la posición final
print("The final position is:", final_position)
#Aquí le digo al usuario cual es la posición final