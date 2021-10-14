import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

number_name = len(names)

random_choice = random.randint(0, number_name-1)
pay_names = names[random_choice]

print(f"{pay_names} is going to buy the meal today!")
