# Implement your is_colorful method below
def is_colorful(num):
    digits = [int(d) for d in str(num)]
    products = set()

    for start in range(len(digits)):
        product = 1
        for end in range(start, len(digits)):
            product *= digits[end]
            if product in products:  
                return False
            products.add(product)
    return True


# Do not modify the code below:
print("##########################################")
print("###################TESTS###################")
print("##########################################\n")
import os

print("Testing that is colorful returns a bool:")
if type(is_colorful(263)) == bool:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing that is_colorful returns True correctly:")
print("Testing 49:")
if is_colorful(49) == True:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
print("Testing 263:")
if is_colorful(263) == True:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
print("Testing 734:")
if is_colorful(734) == True:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing that is_colorful returns False correctly:")
print("Testing 51:")
if is_colorful(51) == False:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
print("Testing 236:")
if is_colorful(236) == False:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
print("Testing 781:")
if is_colorful(781) == False:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")