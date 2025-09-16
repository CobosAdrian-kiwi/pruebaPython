#Empieza la funcion
def lower_num(num1,num2):
    if num1 <= num2:
        lowest = num1
    else:
        lowest = num2
    return lowest
        #Termina la funcion
first_num = int(input("Enter the first number:"))
second_num = int(input("Enter the second number:"))

print("El más pequeño es: " + str(lower_num(first_num, second_num)))