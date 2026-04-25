# Task 1: Tuple swap

a = 5
b = 10

a, b = b, a

print(a, b)


# Task 2: Set intersection

set1 = {"Tom", "Jerry", "Hewey", "Dewey", "Louie"}
set2 = {"Tom", "Garfield", "Snoopy", "Hewey", "Dewey"}

common = set1.intersection(set2)
print(common)


# Task 3: Histogram (dictionary)

def histogram(lst):
    result = {}

    for item in lst:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result


my_list = [1, 2, 3, 1, 2, 3, 4]

print(histogram(my_list))

assert histogram(my_list) == {1: 2, 2: 2, 3: 2, 4: 1}


from abc import ABC, abstractmethod
from random import randint


class Dice(ABC):
    def __init__(self):
        self.face = None

    @abstractmethod
    def roll(self):
        pass


class SixSidedDice(Dice):
    def roll(self):
        self.face = randint(1, 6)
        return self.face


class TenSidedDice(Dice):
    def roll(self):
        self.face = randint(1, 10)
        return self.face


# Test

dice = SixSidedDice()
results = []

for _ in range(1000):
    results.append(dice.roll())

print(histogram(results))