def roman_to_int(s: str) -> int:
    roman_dict = {
        "I": 1, "V": 5, "X": 10,
        "L": 50, "C": 100, "D": 500, "M": 1000
    }
    
    total = 0
    prev_val = 0
    
    for char in s:
        current_val = roman_dict[char]
        total += current_val
        if current_val > prev_val: 
            total -= 2 * prev_val
        prev_val = current_val
    
    return total

# Do not modify the code below:
print("##########################################")
print("##################TESTS###################")
print("##########################################\n")
import os

print("Testing with 4")
if roman_to_int("IV") == 4:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with 12")
if roman_to_int("XII") == 12:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with 14")
if roman_to_int("XIV") == 14:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with 19")
if roman_to_int("XIX") == 19:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with 49")
if roman_to_int("XLIX") == 49:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with 78")
if roman_to_int("LXXVIII") == 78:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with 79")
if roman_to_int("LXXIX") == 79:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with 101")
if roman_to_int("CI") == 101:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing 499")
if roman_to_int("CDXCIX") == 499:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing 1006")
if roman_to_int("MVI") == 1006:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing with 1989")
if roman_to_int("MCMLXXXIX") == 1989:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")


    
    
    
    
