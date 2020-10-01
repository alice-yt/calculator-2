"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

# Replace this with your code

calculator = True
while calculator == True: 
    input_string = input('>')
    token = input_string.split(' ')
    if token[0] == 'q':
        calculator = False
    else:
        a = int(token[1])
        if token[0] == '+':
            b = int(token[2])
            x = add(a, b)
        elif token[0] == '-':
            b = int(token[2])
            x = subtract(a,b)
        elif token[0] == '*':
            b = int(token[2])
            x = multiply(a,b)
        elif token[0] == '/':
            b = int(token[2])
            x = divide(a,b)
        elif token[0] == 'square':
            x = square(a)
        elif token[0] == 'cube':
            x = cube(a)
        elif token[0] == 'pow':
            b = int(token[2])
            x = power(a,b)
        elif token[0] == 'mod':
            b = int(token[2])
            x = mod(a,b)
        print(x)

        

