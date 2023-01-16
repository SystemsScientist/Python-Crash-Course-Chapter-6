# exercise_06_12.py, Chapter 6, Python Crash Course
# 
# Extensions: We're new working with examples that 
# are complex enough that they can be extended in
# any number of ways. Use one of the example programs
# from this chapter, and extend it by adding new keys
# and values, changing the context of the program or
# improving the formatting of the output. 

cities = {
            'minneapolis': {
                'state': 'minnesota',
                'country': 'united states',
                'population': 425000,
                'incorporated': 1867,
                'population rank': 46,
            },
            'dallas': {
                'state': 'texas',
                'country': 'united states',
                'population': 130000,
                'incorporated': 1856,
                'population rank': 9,
            },
            'new york city': {
                'state': 'new york',
                'country': 'united states',
                'population': 8800000,
                'incorporated': 1898,
                'population rank': 1,
            },
            'los angeles': {
                'state': 'california',
                'country': 'united states',
                'population': 3900000,
                'incorporated': 1850,
                'population rank': 2,
            },
        }

for city, city_info in cities.items():
    print("\nCity: " + city.title())
    print("\tCountry: " + city_info['country'].title())
    print("\tPopulation: " + str(city_info['population']))
    print("\tIncorporated: " + str(city_info['incorporated']))
    
    if city_info['population rank'] == 1:
        print("\tPopulation Rank: " + str(city_info['population rank']) + "st")
    elif city_info['population rank'] == 2:
        print("\tPopulation Rank: " + str(city_info['population rank']) + "nd")
    else:
        print("\tPopulation Rank: " + str(city_info['population rank']) + "th")



