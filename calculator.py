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
        #[add, subtr, mult] = operators   operator[0] CALL FUNCTION SOMEHOW
            #for loop inside operators to see where it is ==, and get idx

while True:
    equation = input("> ")
    tokens = equation.split(" ")
    
    operator = tokens[0]
    
    if operator == "q":
        break
    elif operator == "+":
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        print(add(num1,num2))
    elif operator == "-":
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        print(subtract(num1, num2))
    elif operator == "*":
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        print(multiply(num1, num2))
    elif operator == "/":
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        print(divide(num1, num2))
    elif operator == "square":
        num1 = int(tokens[1])
        print(square(num1))
    elif operator == "cube":
        num1 = int(tokens[1])
        print(cube(num1))
    elif operator == "pow":
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        print(power(num1, num2))
    elif operator  == "%":
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        print(mod(num1, num2))