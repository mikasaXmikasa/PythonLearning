for x in range(0, 5):
    print(x)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(0, 11, 2))
print(even_numbers)


# square numberrs

squares = []

for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)


print(min(squares))
print(max(squares))
print(sum(squares))


# List Comprehensions

new_squares = [value ** 2 for value in range(1, 11)]
print(new_squares)

# SLICING A LIST

players = ['charles', 'martina', 'micheal', 'florence', 'eli']

print(players[0:3])

print(players[1:4])

print(players[:4])

print(players[-3:])

# COPYING

my_foods = ['pizza', 'pasta', 'carrot cake']
friend_foods = my_food[:]

friend_foods.insert(1, "rice")

print("My favourite foods are: ")
print(my_foods)

print("\n My friend's favourite foods are:")
print(friend_foods)

