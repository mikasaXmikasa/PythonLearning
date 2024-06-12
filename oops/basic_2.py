class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.open = False


    def describe_restaurant(self):
        """Describe the Restaurant name and cuisine type"""
        print(f"\nOur restaurant's name is {self.restaurant_name} and we offer {self.cuisine_type}")

    def open_restaurant(self):
        """opens the restaurant"""
        self.open = True
        print("\nOpening the restaurant")

restaurant1 = Restaurant("Chillies", "Italian")
restaurant2 = Restaurant("Storos", "Mexican")
restaurant3 = Restaurant("Chawlas", "Indian")

restaurants = [restaurant1, restaurant2, restaurant3]

print(f"Restaurant's name is {restaurant1.restaurant_name} and cuisine's type is {restaurant1.cuisine_type}")   


for restaurant in restaurants:
    restaurant.describe_restaurant()



class Users:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_restaurant(self):
        print(f"User's first name is {self.first_name} and last name is {self.last_name}")


    def greet_user(self):
        print(f"Hi, {self.first_name}. Nice to have you here")


user1 = Users("Aryan", "Goyal")
user2 = Users("Narun", "Jindal")

user1.greet_user()
user2.greet_user()