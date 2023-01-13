# favorite_languages2.py, Chapter 6, Python Crash Course
# program initializes a dictionary or users and favorite
# programming languages and uses a for loop, an items()
# method, and print statement

favorite_languages = {
                      'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',
                      }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")



