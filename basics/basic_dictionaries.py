alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# adding new key-value pairs

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# delete key-value pair

del alien_0['points']

print(alien_0)


# Using get to access the values so we can also handle the error if key is not found

point_value = alien_0.get('points', 'No Point Value assigned')
# if alternate value is not given it will give back 'None'
print(point_value)


user_0 = {
    'username': 'aryanngoyal',
    'firstname': 'Aryan',
    'lastname': 'Goyal'
}


for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())

# you can use favourite_languages as it is because its a default behavious


# this does not filter out repeats values although
for language in favorite_languages.values(): 
    print(language.title())

#  to filter out repeats

for language in set(favorite_languages.values()):
    print(language.title())


# List of dictionaries

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]


aliens[0]["x_position"] = 20

print(aliens[0])

ref_to_alien0 = aliens[0]

ref_to_alien0['y_position'] = 10

print(aliens[0])


# a list in a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
