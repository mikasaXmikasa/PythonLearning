bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# accessing elements in a list 

print(bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])


# accessing elements in a list from the end - start from -1 from the behind

print(bicycles[-1])
print(bicycles[-2])

# modifying, adding and removing elements


# modifying 

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles[-2] = 'royal enfield'
print(motorcycles)



# add elements to the list

# adding

motorcycles.append('harley')
print(motorcycles)

# inserting

# for positive index it inserts at the position of index
motorcycles.insert(1, "hero")
print(motorcycles)

# but for neg index it inserts it to the left of that index
motorcycles.insert(-1, "Kawasaki")
print(motorcycles)  

# removing an item

del motorcycles[-2]
print(motorcycles)


# removing an item using pop method

last_motorcycle = motorcycles.pop()
print(last_motorcycle)
print(motorcycles)

# you can also use index to remove an element you want

second_motorcycle_popped = motorcycles.pop(1)
print(second_motorcycle_popped)

# removing an item by value


# remove the first element that matches the given object
motorcycles.remove('ducati')
print(motorcycles)

# Organizing a list

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# in reverse order

cars.sort(reverse=True)
print(cars)


# get a copy of the sorted list

sorted_cars = sorted(cars, reverse=True)
print(sorted_cars)


# printing a list in reverse order

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)


length_of_cars = len(cars)
print(length_of_cars)

