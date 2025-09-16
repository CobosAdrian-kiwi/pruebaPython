def highest_number(num1, num2, num3): #Denfino la funcion que tenga 3 variables
    if num1 >= num2 and num1 >= num3: 
        highest = num1
    else:
        if num2 >= num1 and num2 >= num3:
            highest = num2
        else: highest = num3
    return highest
#Si num1 es mayor que los otros 2 entonces fijamos num1 como highest
#Si num1 no es mayor que los otros 2 entonces comprobamos que num2 es mayor que num1 y num3
#Si la comprobacion de num2 como el mayor es correcta num2 es el highest
#Si ninguno ha funcionado entonces tiene que ser el num3 el highest

first_num = int(input("Enter the first number:"))
second_num = int(input("Enter the second number:")) #Preguntamos al usuario
third_num = int(input("Enter the third number:"))

print("El más grande es " + str(highest_number(first_num, second_num, third_num)))
#Imprimimos "El más grande es" y convertimos el resultado de ejecutar la funcion con las
#variables que hemos preguntado al usuario a string y la concatenamos
