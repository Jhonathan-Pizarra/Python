# a list comprehension
# List comprehensions are a useful way of quickly creating lists whose contents obey a simple rule.
cubes = [i**3 for i in range(5)]

print(cubes)

#Compresiones condicionales
evens=[i**2 for i in range(10) if i**2 % 2 == 0]

print(evens)