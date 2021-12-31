#Diccionarios
#Dictionaries are data structures used to map arbitrary keys to values.
#Lists can be thought of as dictionaries with integer keys within a certain range.
#Each element in a dictionary is represented by a key:value pair.

ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])

primary = {
    "red": [255, 0, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255],
}

print(primary["red"])
# print(primary["yellow"]) Trying to index a key that isn't part of the dictionary returns a KeyError.

#Accedear a valores
squares = {1: 1, 2: 4, 3: "error", 4: 16,}
squares[8] = 64
squares[3] = 9
print(squares) # respuesta: {1: 1, 2: 4, 3: 9, 4: 16, 8: 64}

#No en la lista
nums = {
    1: "one",
    2: "two",
    3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

#Get
fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5)) # 3 + 5

#Tuplas sin parentesis
my_tuple = "one", "two", "three"
print(my_tuple[0])