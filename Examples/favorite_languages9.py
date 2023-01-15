# favorite_languages9.py, Chapter 6, Python Crash Course
# program prints users favorite languages

favorite_languages = {
                        'jen': ['python', 'ruby'],
                        'sarah': ['c'],
                        'edward': ['ruby', 'go'],
                        'phil': ['python', 'haskell'],
                    }

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are: ")
    for language in languages:
        print("\t" + language.title())



