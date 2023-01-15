# pizza.py, Chapter 6, Python Crash Course
# program prints pizza toppings

# Store information about a pizza being ordered
pizza = {
            'crust': 'thick',
            'toppings': ['mushrooms', 'extra cheese'],
        }

# Summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings: ")

for topping in pizza['toppings']:
    print("\t" + topping)



