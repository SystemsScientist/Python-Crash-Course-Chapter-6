# favorite_languages5.py, Chapter 6, Python Crash Course
# program initializes a dictionary and checks if all
# users have taken the poll

favorite_languages = {
                        'jen': 'python',
                        'sarah': 'c',
                        'edward': 'ruby',
                        'phil': 'python',
                    }

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll.")



