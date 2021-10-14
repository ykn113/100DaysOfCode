print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name12 = name1 + name2

name12.lower()

t = name12.count("t")
r = name12.count("r")
u = name12.count("u")
e = name12.count("e")

true = t + r + u + e

l = name12.count("l")
o = name12.count("o")
v = name12.count("v")
e = name12.count("e")
love = l + o + v + e

love_score = int(str(true)+ str(love))

if (love_score < 10) or (love_score > 90):
  print(f"Your score is {love_score}, you go together loke coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
