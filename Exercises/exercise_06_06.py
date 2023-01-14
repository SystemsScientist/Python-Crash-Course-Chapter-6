# exercise_06_06.py, Chapter 6, Python Crash Course
# 
# Polling: Use the code in favorite_languages.py (page 104).

favorite_languages = {
                        'jen': 'python',
                        'sarah': 'c',
                        'edward': 'ruby',
                        'phil': 'python',
                    }

#   - Make a list of people who should take the favorite 
#     languages poll. Include some names that are already
#     in the dictionary and some that are not.

friends = ['ted', 'stephanie', 'jen', 'sarah', 'phil', 'joseph', 'jennifer']

#   - Loop through the list of people who should take the
#     poll. If they have already taken the poll, print a
#     message thanking them for responding. If they have
#     not yet taken the poll, print a message inviting
#     them to take the poll.

for name in friends[:]:
    if name in favorite_languages:
        print("Thank you for taking our poll, " + name.title() + ".")
    else:
        print("We invite you to take our poll, " + name.title() + ".")



