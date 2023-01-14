# aliens.py, Chapter 6, Python Crash Course
# program initializes multiple dictionaries,
# adds multiple dictionaries to a list, and
# uses a for loop to print the dictionaries

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)



