# exercise_06_04.py, Chapter 6, Python Crash Course
#
# Glossary 2: Now that you know how to loop through
# a dictionary, clean up the code from exercise_06_04.py
# by replacing your series of print statements with a 
# loop that runs through the dictionary's keys and
# values. When you're sure that your loop works, add
# five more Python terms to your glossary. When you
# run your program again, these new words and meanings
# should automatically be included in the output.

glossary = {
            'dictionary': 'a dictionary in Python is a collection of key-value pairs',
            'if statement': 'allow you to examine the current state of a program',
            'list': 'a collection of items in a particular order',
            'string': 'is a series of characters',
            'comments': 'anything following a hash mark (#) in your code is ignored',
           }

for key, value in glossary.items():
    if key == 'list':
        print(key.title() + ": " + "\t\t" + value + "\n")
    elif key == 'if statement':
        print(key + ": " + "\t" + value + "\n")
    else:
        print(key.title() + ": " + "\t" + value + "\n")



