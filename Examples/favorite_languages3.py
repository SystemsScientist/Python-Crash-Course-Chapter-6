# favorite_languages3.py, Chapter 6, Python Crash Course
# program initializes a dictionary or users and favorite
# programming languages and uses a for loop, a key()
# method and a print statement

favorite_languages = {
                        'jen': 'python',
                        'sarah': 'c',
                        'edward': 'ruby',
                        'phil': 'python',
                    }

for name in favorite_languages.keys():
    print(name.title())



