# favorite_languages7.py, Chapter 6, Python Crash Course
# program returns only the values

favorite_languages = {
                        'jen': 'python',
                        'sarah': 'c',
                        'edward': 'ruby',
                        'phil': 'python',
                    }

print("The following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title())



