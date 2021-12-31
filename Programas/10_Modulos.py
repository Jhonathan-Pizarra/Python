import random
#Modules are pieces of code that other people have written to fulfill common tasks, such as generating random numbers, performing mathematical operations, etc.
#The basic way to use a module is to add import module_name at the top of your code, and then using module_name.var to access functions and values with the name var in the module.

for i in range(5):
    value = random.randint(1, 6)
    print(value)


#We can get just specific functions from a library using
from math import pi

print(pi)


#Alias para modulos
from math import sqrt as square_root
print(square_root(100))






















