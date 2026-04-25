# Exercise 1: Comparison Operators

x = 5
y = 4

print(x > y)
print(x < y)
print(x == y)
print(x != y)
print(x >= y)
print(x <= y)


# Exercise 2: Logical Operators

age = 25
is_in_age_range = age > 20 and age < 30
print(is_in_age_range)


# Exercise 3: if

age = 19
age_group = "child"

if age > 18:
    age_group = "adult"

print(f"The age group is {age_group}")


# Exercise 4: if-else

wind_speed = 30

if wind_speed < 10:
    print("It is a calm day")
else:
    print("It is a windy day")


# Exercise 5: if-elif-else

grade = 55

if grade < 50:
    print("You failed")
elif grade < 60:
    print("You passed")
elif grade < 70:
    print("You got a good pass")
else:
    print("You got an excellent pass")


# Summary Task: Compare Temperatures

temperature1 = 25
temperature2 = 30

if temperature1 == temperature2:
    print("Temperatures are equal")
else:
    print("Temperatures are not equal")


# Lists

city_list = ["Glasgow", "London", "Edinburgh"]

print(city_list[2])
print(city_list[-2:])

city_list.append("Manchester")
city_list[1] = "Birmingham"


# List Summary Task

colours = ["red", "blue", "green"]

print(colours)
print(colours[1])

colours[0] = "yellow"
print(colours)

print(len(colours))

if "red" in colours:
    print("Red is in the list")

selected_colours = colours[1:3]
print(selected_colours)


# While Loop

i = 0
while i < 5:
    print(i)
    i += 1


# For Loop

for city in city_list:
    print(city)


# Range + Break

for i in range(5):
    if i == 3:
        break
    print(i)


# Continue

for i in range(5):
    if i == 2:
        continue
    print(i)


# Even Numbers

numbers = list(range(1, 11))

for num in numbers:
    if num % 2 == 0:
        print(num)


# Sum of Squares

sum_of_squares = 0

for i in range(1, 6):
    sum_of_squares += i ** 2

print(sum_of_squares)


# Countdown

countdown = 10

while countdown > 0:
    print(countdown)
    countdown -= 1

print("Complete!")


# User Input Task 1

age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
elif age <= 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


# User Input Task 2

celsius_input = float(input("Enter temperature in Celsius: "))

degree_f = (celsius_input * 9/5) + 32
degree_k = celsius_input + 273.15

print(f"{celsius_input}C = {degree_f}F")
print(f"{celsius_input}C = {degree_k}K")