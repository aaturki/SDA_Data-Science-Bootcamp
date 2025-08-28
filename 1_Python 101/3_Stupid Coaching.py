# Implement your coach_answer method below:
def coach_answer(your_message):
    if your_message == "I am going to work right now!":
        return ""
    if your_message.endswith("?"):
        return "Silly question, get dressed and go to work!"
    return "I don't care, get dressed and go to work!"



# Implement your coach_answer_enhanced below:
def coach_answer_enhanced(your_message):
    if your_message == "I AM GOING TO WORK RIGHT NOW!":
        return ""
    if your_message.isupper():
        return "I can feel your motivation! " + coach_answer(your_message)
    return coach_answer(your_message)


# Do not modify the code below:
print("##########################################")
print("###################TESTS###################")
print("##########################################\n")

import os
print("Testing coach_answer method")
print("------------------------------------------------------------------------\n")

print("Testing that coach_answer returns a str")
if type(coach_answer("Hello coach!")) == str:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing that coach_answer replies saying he does not care when you enter a statement")
if coach_answer("I would love to eat some pizza!")  == "I don't care, get dressed and go to work!":
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing that coach_answer replies saying it\'s a silly question when you enter a question")
if coach_answer("Can I eat some pizza?") == "Silly question, get dressed and go to work!":
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing that coach_answer does not answer back (i.e. answers with an empty string) when you tell him you are going to work")
if coach_answer( "I am going to work right now!" ) == "":
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("\n")
print("Testing coach_answer_ennhanced method")
print("------------------------------------------------------------------------\n")

print("Testing that coach_answer_enhanced returns a str")
if type(coach_answer_enhanced("Hello coach!")) == str:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing that coach_answer_enhanced replies saying he does not care when you enter a statement (and does not shout)")
if coach_answer_enhanced("I would love to eat some pizza!") == "I don't care, get dressed and go to work!":
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing that coach_answer_enhanced replies saying it\'s a silly question when you enter a question (and does not shout)")
if coach_answer_enhanced("Can I eat some pizza?") == "Silly question, get dressed and go to work!":
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing that coach_answer_enhanced does not answer back (i.e. answers with an empty string) when you tell him you are going to work (and does not shout)")
if coach_answer_enhanced( "I am going to work right now!" ) == "":
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing that coach_answer_enhanced prepends a motivation statement before saying he does not care when you shout a statement at him")
if coach_answer_enhanced("I WOULD LOVE SOME PIZZA!") == "I can feel your motivation! I don't care, get dressed and go to work!":
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing that coach_answer_enhanced prepends a motivation statement before saying that it\'s a silly question when you shout a question at him")
if coach_answer_enhanced("CAN I EAT SOME PIZZA?") == "I can feel your motivation! Silly question, get dressed and go to work!":
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing that coach_answer_enhanced does not answer back (i.e. answers with an empty string) when you shout at him saying you are going to work")
if coach_answer_enhanced( "I AM GOING TO WORK RIGHT NOW!" ) == "":
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")