DISHES_CALORIES = {
    "Hamburger": 250,
    "Cheese Burger": 300,
    "Big Mac": 540,
    "McChicken": 350,
    "French Fries": 230,
    "Salad": 15,
    "Coca Cola": 150,
    "Sprite": 150
}

def poor_calories_counter(*dishes):
    total = 0
    for dish in dishes:
        if dish not in DISHES_CALORIES:
            return f"{dish} not found"
        total += DISHES_CALORIES[dish]
    return total

# Do not modify the code below:
print("##########################################")
print("##################TESTS###################")
print("##########################################\n")

import os
print("Testing with Hamburger, Cheese Burger, Big Mac")
if poor_calories_counter("Hamburger", "Cheese Burger", "Big Mac") == 1090:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with Big Mac, Salad, Coca Cola")
if poor_calories_counter("Big Mac", "Salad", "Coca Cola") == 705:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing with McChicken, French Fries, Sprite")
if poor_calories_counter("McChicken", "French Fries", "Sprite") == 730:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with Shrimp, French Fries, Salad")
if poor_calories_counter("Shrimp", "French Fries", "Salad") == 'Shrimp not found':
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")