#storage of data in key-value pairs
#dictionary is a collection of key-value pairs
#keys are unique and immutable
#values can be of any data type and can be duplicated
#dictionaries are unordered and mutable
#creating a dictionary
data = {
    "x": 1,
    "y": 2,
    "z": 3
}
print(data)
print(type(data))

b = dict(name="Alice", age=30, city="New York")
print(b)

#accessing dictionary items
print(b["name"])

#using get method
print(b.get["age"])

#remving
del b["city"]

num = b.pop("age")
print(num)