num = [5, 10, 15, 20]
print(num[0])  # Output: 5
print(num[1])  # Output: 10
print(num[2])  # Output: 15

#using constructor
num2 = list((1, 2, 3, 4))
print(num2)  # Output: [1, 2, 3, 4
print(num2[-3])  # Output: 2

#list slicing
print(num[1:3])  # Output: [10, 15]

# implement srep: replace a slice of a list and return a new list

def srep(sequence, start=None, stop=None, replacement=None):
    """Return a new list with the slice sequence[start:stop] replaced.

    replacement can be any iterable. If omitted, the slice is removed.
    """
    if replacement is None:
        replacement = []
    result = list(sequence)
    result[start:stop] = list(replacement)
    return result

# demo of srep
numbers = [1, 2, 3, 4, 5]
print(srep(numbers, 1, 4, [9, 9]))  # Output: [1, 9, 9, 5]
print(numbers)  # original list remains unchanged: [1, 2, 3, 4, 5]

#creating tuples
t = (1, 2, 3, 4)
print(t)  # Output: (1, 2, 3, 4)

#tuples are immutable
# t[0] = 10  # This would raise a TypeError
#creating lists from tuples
num_from_tuple = list(t)
print(num_from_tuple)  # Output: [1, 2, 3, 4]

#deleting elements from a list
del numbers[0]  # Removes the first element
#using pop() to remove and return an element
popped_element = numbers.pop(0)  # Removes and returns the first element
print(popped_element)  # Output: 1

#using remove() to remove an element by value
numbers.remove(3)  # Removes the first occurrence of 3
print(numbers)  # Output: [2, 4, 5]