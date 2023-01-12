# exercise_06_01.py, Chapter 6, Python Crash Course
#
# Person: Use a dictionary to store information about a person
# you know. Store their first name, last name, age, and the 
# city in which they live. You should have keys such as
# first_name, last_name, age, and city. Print each piece
# of information stored in your dictionary.

sg1_actors = {'first_name': 'richard',
              'middle_name': 'dean',
              'last_name': 'anderson',
              'age': 72,
              'city': 'minneapolis',
              }

print("One of the stars of Stargate: SG-1 is ")
print("\tFirst name: " + sg1_actors['first_name'].title())
print("\tMiddle name: " + sg1_actors['middle_name'].title())
print("\tLast name: " + sg1_actors['last_name'].title())
print("\tAge: " + str(sg1_actors['age']))
print("\tCity: " + sg1_actors['city'].title())



