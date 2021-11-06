age = input("What is your current age?")

age = int(age)

years_remaining = 100 - age
days_remaining = years_remaining * 360
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = (f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left.")
print(message)
