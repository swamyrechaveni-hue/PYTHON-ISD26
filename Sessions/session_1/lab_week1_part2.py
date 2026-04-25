# Exercise 1: Variables and Types

var_1 = True      # Type = boolean
var_2 = 1         # Type = integer
var_3 = 3.14159   # Type = float
var_4 = "Hello World"  # Type = string

print(type(var_1))
print(type(var_2))
print(type(var_3))
print(type(var_4))


# Task 2: Casting

my_int = 5
my_float = 5.5
my_bool = True

print(my_int)
print(my_float)
print(my_bool)

my_int_float = float(my_int)
my_float_int = int(my_float)
my_bool_int = int(my_bool)

print(my_int_float)
print(my_float_int)
print(my_bool_int)


# Exercise 2: Arithmetic Operators

result_addition = 10 + 5
print("Addition:", result_addition)

result_subtraction = 20 - 8
print("Subtraction:", result_subtraction)

result_multiplication = 6 * 4
print("Multiplication:", result_multiplication)

result_division = 15 / 3
print("Division:", result_division)

result_floor_division = 17 // 4
print("Floor Division:", result_floor_division)

result_modulus = 17 % 4
print("Modulus:", result_modulus)

result_exponentiation = 2 ** 3
print("Exponentiation:", result_exponentiation)


# Average

num1 = 10
num2 = 20

average = (num1 + num2) / 2
print(f"Average of {num1} and {num2} is {average}")


# Rectangle Area

length = 5
width = 3

area = length * width
print(f"Area of rectangle is {area}")


# Exercise 3: Strings

my_string = "This class covers ISD."
print(my_string)

my_uppercase_string = my_string.upper()
my_lowercase_string = my_string.lower()
my_new_string = my_string.replace("ISD", "Interactive Software Design")
my_string_length = len(my_string)

print(my_uppercase_string)
print(my_lowercase_string)
print(my_new_string)
print(my_string_length)


# f-Strings

my_name = "YourName"
number_of_classes = 4
campus = "YourCampus"

my_text = f"My name is {my_name} and I am studying {number_of_classes} classes in {campus}"
print(my_text)