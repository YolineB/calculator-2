"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
#input - comman (eg pow), numbers
# tokenize by .split(' ') for our input NAME token
#if token[0] == add, then call add(0)
#operator = token[0]
#num1 = token[1]
#num2 = token[2]
#lots of ifs statements


while True:
    equation = input("> ")
    tokens = equation.split(" ")
    
    operator = tokens[0]
    
    if operator == "q":
        break

    num1 = int(tokens[1])
    if len(tokens) > 2:
        num2 = int(tokens[2]) 

    elif operator == "+":
        print(add(num1,num2))
    elif operator == "-":
        print(subtract(num1, num2))
    elif operator == "*":
        print(multiply(num1, num2))
    elif operator == "/":
        print(divide(num1, num2))
    elif operator == "square":
        print(square(num1))
    elif operator == "cube":
        print(cube(num1))
    elif operator == "pow":
        print(power(num1, num2))
    elif operator  == "%":
        print(mod(num1, num2))