# map
def double(n):
    return n * 2
numbers = [5, 6, 7, 8]
result = map(double, numbers)
print(list(result))


## reduce
import functools

numbers = [1, 2, 3, 4]

product = functools.reduce(lambda x, y: x * y, numbers)
print("Product of list elements:", product)


## filter
# Define a function to check if a number is even
def is_even(n):
    return n % 2 == 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(is_even, numbers)
print("Even numbers:", list(even_numbers))



## using map and filter 
#filetr string greater than 4
names = ["apple", "cat", "elelphant", "Dog", "Baseball"]
updated = list(filter(lambda x: len(x) > 4, names))
print(updated)

#
uppercase_name=list(map(str.upper,names))
print(uppercase_name)
