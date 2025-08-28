mcdo = {
    "Hamburger": 250,
    "Cheese Burger": 300,
    "Big Mac": 540,
    "McChicken": 350,
    "French Fries": 230,
    "Salad": 15,
    "Coca Cola": 150,
    "Sprite": 150
}

mcdo2 = {
    "Happy Meal": ["Cheese Burger", "French Fries", "Coca Cola"],
    "Best Of Big Mac": ["Big Mac", "French Fries", "Coca Cola"],
    "Best Of McChicken": ["McChicken", "Salad", "Sprite"]
}

def advanced_calories_counter(order):
    total = 0
    for dish in order:
        if dish in mcdo:
            total += mcdo[dish]
        elif dish in mcdo2:
            for item in mcdo2[dish]:
                if item not in mcdo:
                    return f"{item} not found"
                total += mcdo[item]
        else:
            return f"{dish} not found"
    return total

# Do not modify the code below:
print("##########################################")
print("##################TESTS###################")
print("##########################################\n")
import os

print("Testing with the lot")
if advanced_calories_counter(['Happy Meal', 'Best Of Big Mac', 'Best Of Royal Cheese']) == 'Best Of Royal Cheese not found':
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing with Big Mac, French Fries, Happy Meal, Coca Cola")
if advanced_calories_counter(["Big Mac", "French Fries", "Happy Meal", "Coca Cola"]) == 1600:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Best Of Big Mac, Salad, Happy Meal, Sprite")
if advanced_calories_counter(["Best Of Big Mac", "Salad", "Happy Meal", "Sprite"]) == 1765:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with Happy Meal, McChicken")
if advanced_calories_counter(["Happy Meal", "McChicken"]) == 1030:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with Fish and Chips, Salad")
if advanced_calories_counter(["Fish and Chips", "Salad"]) == 'Fish and Chips not found':
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")