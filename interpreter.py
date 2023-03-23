#Prompts the user for an arithmetic expression and separates inputted str into a sequence of values.
expression = input("Expression: ").split(" ")
# Assigns x variable value of position 0 from separated user input, converts str into int.
x = int(expression[0])
# Assigns y variable value of position 1 from separated user input.
y = expression[1]
# Assigns z variable value of position 2 from separated user input, converts str into int.
z = int(expression[2])
# makes arithmetical calculation, converts output into float.
if y == "+":
    answer = x+z
    print(float(answer))
# makes arithmetical calculation, converts output into float.
elif y == "-":
    answer = x-z
    print(float(answer))
# makes arithmetical calculation, converts output into float value formatted to one decimal place.
elif y == "/":
    if z!=0:
        answer = x/z
        print(float("{:.1f}".format(answer)))
    else:
        print("you can't divide by zero")
# makes arithmetical calculation, converts output into float.
elif y == "*":
    answer = x*z
    print(float(answer))