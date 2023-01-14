# exercise_06_05.py, Chapter 6, Python Crash Course
# 
# Rivers: Make a dictionary containing three major rivers
# and the country each river runs through. One key-value
# pair might be 'nile': 'egypt'.

rivers_glossary = {
                    'nile': 'egypt',
                    'mississippi': 'united states',
                    'amazon': 'brazil',
                  }

#   - Use a loop to print a sentence about each river,
#     such as "The Nile runs through Egypt".

print("\nRivers and Countries: ")
for key, value in rivers_glossary.items():
    if key == 'mississippi':
        print("The " + key.title() + " river runs through the " + value.title() + ".")
    else:
        print("The " + key.title() + " river runs through " + value.title() + ".")

#   - Use a loop to print the name of each river included
#     in the dictionary.

print("\nRivers: ")
for key, value in rivers_glossary.items():
    print(key.title())

#   - Use a loop to print the name of each country included
#     in the dictionary.

print("\nCountries: ")
for key, value in rivers_glossary.items():
    print(value.title())
print("\n")



