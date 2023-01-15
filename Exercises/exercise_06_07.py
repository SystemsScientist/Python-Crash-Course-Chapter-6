# exercise_06_07.py, Chapter 6, Python Crash Course
#
# People: Start with the program you wrote for exercise_06_01.py.
# Make two new dictionaries representing different people, and
# store all three dictionaries in a list called people. Loop
# through your list of people. As you loop through the list,
# print everything you know about each person.

sg1_actor1 = {
                'first_name': 'richard',
                'last_name': 'anderson',
                'age': 72,
                'city': 'minneapolis',
            }

sg1_actor2 = {
                'first_name': 'michael',
                'last_name': 'shanks',
                'age': 52,
                'city': 'vancouver',
            }

sg1_actor3 = {
                'first_name': 'amanda',
                'last_name': 'tapping',
                'age': 57,
                'city': 'rochford',
            }

sg1_actor4 = {
                'first_name': 'christopher',
                'last_name': 'judge',
                'age': 58,
                'city': 'los angeles',
            }

people = [sg1_actor1, sg1_actor2, sg1_actor3, sg1_actor4]

print("\nList of Stargate Sg-1 Actors: \n")
for person in people:
    print("First name: " + person['first_name'].title())
    print("Last name: " + person['last_name'].title())
    print("Age: " + str(person['age']))
    print("City: " + person['city'].title() + "\n")


