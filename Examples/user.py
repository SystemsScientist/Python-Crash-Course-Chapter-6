# user.py, Chapter 6, Python Crash Course
# program initializes a dictionary and use
# a for loop, an items() method, and print 
# statements

user_0 = {'username': 'efermi',
          'first': 'enrico',
          'last': 'fermi',
          }

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)



