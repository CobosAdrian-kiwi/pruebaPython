def highest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        highest = num1
    else:
        if num2 >= num1 and num2 >= num3:
            highest = num2
        else: highest = num3
    return highest

first_num = int(input("Enter the first number:"))
second_num = int(input("Enter the second number:"))
third_num = int(input("Enter the third number:"))

print("El más grande es " + str(highest_number(first_num, second_num, third_num)))