# Implement your simple_calculator function below
def simple_calculator(arguments):
    if len(arguments) != 3:
        return 'Please enter valid format: [Operand, Operator, Operand]'
    
    operand1_str, operator, operand2_str = arguments
    valid_operators = ['+', '-', '*', '/', '%']
    
    if operator not in valid_operators:
        return 'Please enter a valid operator [ +, -, /, *, % ]'
    
    operand1 = float(operand1_str)
    operand2 = float(operand2_str)
    
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
    elif operator == '%':
        return operand1 % operand2


# Do not modify the code below:
print("##########################################")
print("##################TESTS###################")
print("##########################################\n")

import os
print("Testing your function's addition:")
if simple_calculator(['5', '+', '5']) == 10:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing your function's subtraction:")
if simple_calculator(['10.5', '-', '5']) == 5.5:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing your function's multiplication:")
if simple_calculator(['8', '*', '8']) == 64:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing your function's division:")
if simple_calculator(['1', '/', '4']) == 0.25:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing your function's modulo:")
if simple_calculator(['9', '%', '2']) == 1:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing your function's error handling:")
if simple_calculator(['1', '4']) == 'Please enter valid format: [Operand, Operator, Operand]':
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
if simple_calculator(['1', '4', '5', '+']) == 'Please enter valid format: [Operand, Operator, Operand]':
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
if simple_calculator(['1', '&', '5']) == 'Please enter a valid operator [ +, -, /, *, % ]':
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    