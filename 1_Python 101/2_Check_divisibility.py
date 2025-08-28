# Implement your check_divisibility method below:
def check_divisibility(num, a, b):
    return num % a == 0 and num % b == 0


# Do not modify the code below:
print("##########################################")
print("##################TESTS###################")
print("##########################################\n")

import os

print("Testing check_divisibility with num = 12, a = 3, b = 4:")
if check_divisibility(12, 3, 4):
    os.system("echo '\e[32mCorrect\e[0m'")
else:
    os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing check_divisibility with num = 27, a = 9, b = 6:")
if check_divisibility(27, 9, 3):
    os.system("echo '\e[32mCorrect\e[0m'")
else:
    os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing check_divisibility with num = 8, a = 2, b = 5:")
if not check_divisibility(8, 2, 5):
    os.system("echo '\e[32mCorrect\e[0m'")
else:
    os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing check_divisibility with num = 15, a = 4, b = 6:")
if not check_divisibility(15, 4, 6):
    os.system("echo '\e[32mCorrect\e[0m'")
else:
    os.system("echo '\e[31mIncorrect\e[0m'")