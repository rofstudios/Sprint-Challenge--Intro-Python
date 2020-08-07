# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = [d.name for d in humans if d.name[0] == 'D']
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [b.name for b in humans if b.name[-1] == 'e']
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
letters = ['C','D','E','F','G']
c = [c.name for c in humans if c.name[0] in letters] # storing letters in a list and comparing if equal to [0] of name || shorter || works
z = [z.name for z in humans if z.name[0] == 'C' or z.name[0] == 'D' or z.name[0] == 'E' or z.name[0] == 'F' or z.name[0] == 'G'] # a bit longer to write || works
print(c)
print(z)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [d.age + 10 for d in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [f"{e.name}-{str(e.age)}" for e in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(f.name, f.age) for f in humans if f.age > 27 and f.age < 33]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
# g = [(g.name.upper(), g.age + 5) for g in humans]
g = [Human(g.name.upper(), g.age + 5) for g in humans]
# print(humans)

print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
# h = [(h.name, math.sqrt(h.age)) for h in humans]
h = [math.sqrt(h.age) for h in humans]
print(h)

# https://www.geeksforgeeks.org/python-math-function-sqrt/#:~:text=sqrt()%20function%20is%20an,number%20passed%20in%20the%20parameter. ref site
