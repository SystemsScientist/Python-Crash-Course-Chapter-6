# exercise_06_03.py, Chapter 6, Python Crash Course
#
# Glossary: A Python dictionary can be used to model
# an actual dictionary. However, to avoid confusion,
# let's call it a glossary.
#
#   - Think of five programming words you've learned
#     about in the previous chapters. Use these words
#     as the keys in your glossary, and store their
#     meanings as values.

glossary = {'dictionary': 'a dictionary in Python is a collection of key-value pairs',
            'if statement': 'allows you to examine the current state of a program',
            'list': 'a collection of items in a particular order',
            'string': 'is a series of characters',
            'comments': 'anything following a hash mark (#) in your code is ignored',
            }

#   - Print each word and its meanings as neatly
#     formatted output. You might print the word
#     followed by a colon and then its meaning, or
#     print the word on one line and then print its
#     meaning indented on a second line. Use the 
#     newline character (\n) to insert a blank line
#     between each word-meaning pair in your output.

for name in glossary:
    if name == 'list':
        print(name.title() + ": " + "\t\t" + glossary[name] + "\n")
    elif name == 'if statement':
        print(name + ": " + "\t" + glossary[name] + "\n")
    else:
        print(name.title() + ": " + "\t" + glossary[name] + "\n")



