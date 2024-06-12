
def describe_pet(name, animal="Dog", age=None):
    """Describe information about a pet"""
    print(f"\nI have a {animal}")
    print(f"Its name is {name}")
    if age:
        print(f"It is {age} years old")

# Positional Arguments

describe_pet("Bruno", "Dog")

# Keyword Arguments 
describe_pet(name="Terry", animal="Cat")

# Using default values
describe_pet("Jar")

describe_pet("Knine", "Cat", 5)


def print_models(unprinted, printed):
    """3d print a set of models"""
    while unprinted:
        current_model = unprinted.pop()
        print(f"printing {current_model}")
        printed.append(current_model)


original = ["phone case", "pendant", "ring"]
printed = []

# Preventing function to modify the original list
print_models(original[:], printed)

# Collecting an arbitary number of arguments

def make_pizza(size, *toppings):
    """Make a Pizza"""
    print(f"\nMaking a {size} pizza")
    if not toppings:
        print("Are u sure u want a Plain Pizza??")
        return
    print("Toppings")
    for topping in toppings:
        print(f"- {topping}")

make_pizza("small", "pepperoni")
make_pizza("large", "cucumber", "pineapple")
make_pizza("medium", "mushrooms", "peppers", "extra cheese")
make_pizza("medium")

# Collecting a arbitary number of keyword arguments

def build_profile(first, last, **user_info):
    """Build the user profile by the given information"""
    user_info["first"], user_info["last"] = first, last
    return user_info
    
user_0 = build_profile("aryan", "goyal", location="harvard", field="cs")
user_1 = build_profile("garima", "jindal")

print(user_0)
print(user_1)