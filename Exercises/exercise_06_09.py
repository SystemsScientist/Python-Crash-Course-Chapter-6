# exercise_06_09.py, Chapter 6, Python Crash Course
# 
# Favorite Places: Make a dictionary called favorite_places.
# Think of three names to use as keys in the dictionary, and
# store one to three favorite places for each person. To 
# make this exercise a bit more interesting, ask some 
# friends to name a few of their favorite places. Loop
# through the dictionary, and print each person's name and
# their favorite places.

# dictionary of favorite places
favorite_places = {
                    'jennifer': ['machu pichhu', 'the grand canyon', 'rome'],
                    'theodore': ['maui', 'masai mara', 'instanbul'],
                    'cynthia': ['oahu', 'angkor wat', 'london'],
                }

# for loop and prints statements
for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are: ")
    for place in places:
        print("\t" + place.title())
print("\n")



