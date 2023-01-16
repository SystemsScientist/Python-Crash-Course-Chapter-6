# exercise_06_08.py, Chapter 6, Python Crash Course
# 
# Pets: Make several dictionaries, where the name of each
# dictionary is the name of a pet. In each dictionary, 
# include the kind of animal and the owner's name. Store
# these dictionaries in a list called pets. Next, loop
# through your list and as you do print everything you 
# know about each pet.

buddy = {
            'name': 'buddy',
            'type': 'german shepherd', 
            'human': 'matthew',
        }

bella = {
            'name': 'bella',
            'type': 'golden retriever', 
            'human': 'sadie',
        }

daisy = {
            'name': 'daisy',
            'type': 'siberian husky', 
            'human': 'phillip',
        }

rocky = {
            'name': 'rocky',
            'type': 'boxer', 
            'human': 'raquel',
        }

bruno = {
            'name': 'bruno',
            'type': 'british bulldog', 
            'human': 'franklin',
        }

pets = [buddy, bella, daisy, rocky, bruno]

print("\nList of Dogs and their Humans: \n")
for pet in pets:
    print("Name of dog: " + pet['name'].title())
    print("Dog type: " + pet['type'].title())
    print("Name of human: " + pet['human'].title() + "\n")



