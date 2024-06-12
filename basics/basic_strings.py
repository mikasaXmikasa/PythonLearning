# return a string with first letter of every word uppercase and every other character having lower case
# or you can say every wo4rd is converted into title case

name = "aRYAN gagan goyal"
print("name after using title(): " + name.title())


#return a string every char in uppercase
print("name in upper case: " + name.upper())


#return a string with every char in lowercase
print("name in lower case: " + name.lower())


# Using variables in strings

first_name = "aryan"
last_name = "goyal"

# These strings are called f-strings
full_name = f"{first_name} {last_name}"

print(full_name)

print(f"Hello, {full_name.title()}")

# using special characters - \t and \n

print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Stripping whitespaces

favourite_language = ' python '

# rstrip - return a string stripped from right part

print(favourite_language.rstrip())

# lstrip - return a string stripped from left part

print(favourite_language.lstrip())

# you can pass a set of characters if you want to remove 
print(favourite_language.lstrip(" p"))



# Removing prefixes

google_url = "https://google.com"

# obv will remove the prefix if its present 
print(google_url.removeprefix("https://"))


# removing suffixes

print(google_url.removesuffix(".com"))

