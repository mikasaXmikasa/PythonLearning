class Dog:
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!!")



# Thinking of a class as a set of instructions for how to make an instance

my_dog = Dog('Willie', 6)

# accessing object's attributes

print(f"My dog's name is {my_dog.name}")
print(f"My dog's age is {my_dog.age}")

# accessing methods

my_dog.sit()
my_dog.roll_over()


your_dog = Dog('Lucy', 5)

print(f"Your dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old.")