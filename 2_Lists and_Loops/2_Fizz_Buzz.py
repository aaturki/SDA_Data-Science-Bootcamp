def fizz_buzz(n):
    return [
        'FizzBuzz' if i % 3 == 0 and i % 5 == 0
        else 'Fizz' if i % 3 == 0
        else 'Buzz' if i % 5 == 0
        else i
        for i in range(1, n + 1)
    ]
print(fizz_buzz(14))


# Do not modify the code below:
print("##########################################")
print("##################TESTS###################")
print("##########################################\n")

import os
print("Testing your Answer:")
if len(fizz_buzz(5)) == 5:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing your Fizz:")
if fizz_buzz(20).count('Fizz') == 5:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing your Buzz:")
if fizz_buzz(33).count('Buzz') == 4:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing your FizzBuzz:")
if fizz_buzz(50).count('FizzBuzz') == 3:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")