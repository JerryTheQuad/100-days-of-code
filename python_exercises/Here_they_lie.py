### Exercise 1: input 'name' and 'age', count in what year will the user turn 100 years old
name = input('What is your name?')
age = int(input('What is your age?'))
year = str((2020 - age) + 100)
print(name + " will be 100 years old in the year " + year)

### Exercise 2: input an even or odd number, output the type. Then input two numbers and see if they are evenly divided.
number = int(input('Gimme an even or odd number:'))
mod = number % 2
if mod > 0:
    print('This is an odd number')
elif mod % 4 == 0:
    print('This is a multiple of 4')
else:
    print('This is an even number')

num = int(input('Gimme a number to check:'))
check = int(input('Gimme a number to divide by:'))
if num % check == 0:
    print('Damn I good')
else:
    print('Go fuck yourself')

### Exercise 3: a is a list with numbers. b prints out a list with numbers < 5 from a. c prints out numbers < input(num) from a.
a = [1, 3, 4, 5, 7, 8, 9]
#b = [element for element in a if element < 5]
#print(b)
num = int(input('Gimme a fucking number'))
c = [element for element in a if element < num]
print(c)

### Exercise 5: list overlap
#Importing this to randomly generate two lists
import random
#Creating the lists
a = random.sample(range(1, 51), 10)
b = random.sample(range(1, 51), 10)
#Defining the function that will look for similar numbers in both lists without duplicates (set())
def intersection(a, b):
    c = [value for value in set(a) if value in set(b)]
    return c
#Printing similar numbers. Note that the random lists might contain 10 different numbers from 1 to 50. Thus, the result might contain no numbers.
print(intersection(a, b))
