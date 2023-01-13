# exercise_06_02.py, Chapter 6, Python Crash Course
# 
# Favorite Numbers: Use a dictionary to store people's
# favorite numbers. Think of five names, and use them
# as keys in your dictionary. Think of a favorite
# number for each person, and store each as a values in
# your dictionary. Print each person's name and their
# favorite number. For even more fun, poll a few friends
# and get some actual data for your program.

names = {'jack': 47, 'daniel': 29, 'sam': 25,
         'tealc': 42, 'george': 16
         }

for name in names:
    print(name.title() + 
          "'s favorite number is " + 
          str(names[name]) + ".")



