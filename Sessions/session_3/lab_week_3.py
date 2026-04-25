# Functions

def greet_user():
    print("Hello!")

greet_user()


def greet_user_with_name(name):
    print(f"Hello {name}!")

greet_user_with_name("John")


def greet_user_full(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")

greet_user_full("John", "Smith")


def greet_user_default(first_name, last_name, university="UWS"):
    print(f"Hello {first_name} {last_name} from {university}!")

greet_user_default("John", "Smith")
greet_user_default("John", "Smith", "UWS London")


# Task 1: greet_friends

def greet_friends(friend_list):
    for name in friend_list:
        print(f"Hello {name}!")

friend_list = ["John", "Jane", "Jack"]
greet_friends(friend_list)


# Return values

def add_numbers(num1, num2):
    return num1 + num2

result = add_numbers(5, 10)
print(result)


def add_and_multiply_numbers(num1, num2):
    return num1 + num2, num1 * num2

sum_result, product_result = add_and_multiply_numbers(5, 10)
print(sum_result)
print(product_result)


# Task 2: Tax calculation

def calculate_tax(income, tax_rate):
    return income * tax_rate

tax = calculate_tax(50000, 0.2)
print(tax)


# Task 3: Compound interest

def compound_interest(principal, duration, interest_rate):
    if interest_rate < 0 or interest_rate > 1:
        print("Please enter a decimal number between 0 and 1")
        return None

    if duration < 0:
        print("Please enter a positive number of years")
        return None

    for year in range(duration + 1):
        total = principal * (1 + interest_rate) ** year
        print(f"The total amount of money earned by the investment in year {year} is {int(total)} £")

    return int(principal * (1 + interest_rate) ** duration)


result = compound_interest(1000, 5, 0.03)
print(result)


# Assertions

assert compound_interest(1000, 5, 0.03) == 1159

assert 5 > 3, "This should be true"

# Uncomment to see assertion error
# assert 5 < 3, "This will fail"


# Fixing errors (corrected versions)

print("Hello, World!")

favorite_color = "Blue"
print("My favorite color is", favorite_color)

number1 = 5
number2 = 3
result = number1 + number2
print("The sum is:", result)

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

time = 11
if time < 12:
    print("Good morning!")