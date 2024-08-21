 # Variables
my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

print(my_string_variable, my_int_variable, my_bool_variable)

# Built-in functions

print(len(my_int_to_str_variable)) # Spaces included
print(len(my_string_variable))


# Variables in the same line
name, surname, alias, age = "Ingrid", "Salvador", 'Ingrid21', 20
print(name, surname, age, "My alias is:", alias)

# Inputs 
name = input('What is your name: ')
age = input('How old are you? ')

print(name)
print(age)

# Not forcing data type, just for us
address: str = "My address"
print(type(address))