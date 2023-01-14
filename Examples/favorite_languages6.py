# favorite_languages6.py, Chapter 6, Python Crash Course
# program initializes a dicitonary and prints the user
# names and favorite languages

favorite_languages = {
                        'jen': 'python',
                        'sarah': 'c',
                        'edward': 'ruby',
                        'phil': 'python',
                    }

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")



