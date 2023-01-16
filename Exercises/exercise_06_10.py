# exercise_06_10.py, Chapter 6, Python Crash Course
# 
# Favorite Numbers: Modify your program from exercise_06_02.py
# so each person can have more than one favorite number. Then
# print each person's name along with their favorite numbers.

# dictionary of names
names = {
            'jack': [47, 13],
            'daniel': [29, 7],
            'sam': [3.14, 6.28],
            'tealc': [42, 42],
            'george': [16],
        }

# for loop and print statements
for name, numbers in names.items():
    print("\n" + name.title() + "'s favorite numbers are: ")
    for number in numbers:
        print("\t" + str(number))
print("\n")



