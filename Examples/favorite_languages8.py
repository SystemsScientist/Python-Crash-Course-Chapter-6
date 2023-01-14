# favorite_languages8.py, Chapter 6, Python Crash Course
# program uses a set() to return the dictionary values

favorite_languages = {
                        'jen': 'python',
                        'sarah': 'c',
                        'edward': 'ruby',
                        'phil': 'python',
                    }

print("The following languages have been mentioned: ")
for language in set(favorite_languages.values()):
    print(language.title())



