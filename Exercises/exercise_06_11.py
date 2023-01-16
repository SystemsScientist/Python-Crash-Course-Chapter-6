# exercise_06_11.py, Chapter 6, Python Crash Course
# 
# Cities: Make a dictionary called cities. Use the
# names of three cities as keys in your dictionary.
# Create a dictionary of information about each city
# and include the country that the city is in, its
# approximate population, and one fact about that
# city. The keys for each city's dictionary should
# be something like country, population, and fact.
# Print the name of each city and all of the 
# information you have stored about it.

cities = {
            'minneapolis': {
                'country': 'united states',
                'population': 425000,
                'fact': 'home of Prince, the musician',
            },
            'dallas': {
                'country': 'united states',
                'population': 1300000,
                'fact': 'home of the Dallas Cowboys',
            },
            'stockholm': {
                'country': 'sweden',
                'population': 2400000,
                'fact': 'on the Baltic Sea',
            },
        }

for city, city_info in cities.items():
    print("\nCity: " + city.title())
    print("\tCountry: " + city_info['country'].title())
    print("\tPopulation: " + str(city_info['population']))
    print("\tFact: " + city_info['fact'])



