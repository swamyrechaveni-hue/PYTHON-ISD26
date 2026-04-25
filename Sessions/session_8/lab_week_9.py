# Task 1: Tuple swap
# Demonstrates Python's tuple unpacking to swap values without a temporary variable
a = 5
b = 10

a, b = b, a

print(a, b)


# Task 2: Set intersection
# Finds common elements between two sets using built-in set operation
set1 = {"Tom", "Jerry", "Hewey", "Dewey", "Louie"}
set2 = {"Tom", "Garfield", "Snoopy", "Hewey", "Dewey"}

common = set1.intersection(set2)
print(common)


# Task 3: Histogram (dictionary)
# Builds a frequency dictionary counting occurrences of elements in a list
def histogram(lst):
    result = {}

    for item in lst:
        # Increment count if item already exists, otherwise initialize it
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result


my_list = [1, 2, 3, 1, 2, 3, 4]

print(histogram(my_list))

# Assertion used to validate correctness of the histogram function
assert histogram(my_list) == {1: 2, 2: 2, 3: 2, 4: 1}


from abc import ABC, abstractmethod
from random import randint


# Abstract base class defining a generic dice structure
class Dice(ABC):
    def __init__(self):
        # Stores the current face value after a roll
        self.face = None

    @abstractmethod
    def roll(self):
        """
        Abstract method to enforce implementation in subclasses.
        """
        pass


# Concrete implementation of a standard 6-sided dice
class SixSidedDice(Dice):
    def roll(self):
        # Generates a random number between 1 and 6
        self.face = randint(1, 6)
        return self.face


# Concrete implementation of a 10-sided dice
class TenSidedDice(Dice):
    def roll(self):
        # Generates a random number between 1 and 10
        self.face = randint(1, 10)
        return self.face


# Test
# Simulates rolling a six-sided dice multiple times and records outcomes
dice = SixSidedDice()
results = []

for _ in range(1000):
    results.append(dice.roll())

# Displays frequency distribution of dice outcomes using histogram function
print(histogram(results))