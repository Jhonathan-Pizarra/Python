#Programacion Funcional
#Es un estilo de progracion badado en funciones
#A key part of functional programming is higher-order functions.
def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10)) #The function apply_twice takes another function as its argument, and calls it twice inside its body.

#Funciones Puras
def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)

#Funciones impuras
some_list = []

def impure(arg):
  some_list.append(arg)

#Funciones Lambdas o anónimas
#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambdas
print((lambda x: x**2 + 5*x + 4) (-4))

#Lambdas en variables
double = lambda x: x * 2
print(double(7))

triple = lambda x: x * 3
add = lambda x, y: x + y
print(add(triple(3), 4))

# Map y Filter
#The function map takes a function and an iterable as arguments, and returns a new iterable with the function applied to each argument
def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums)) #To convert the result into a list, we used list explicitly
print(result)

#Usando la sintaxis lambda:
nums = [11, 22, 33, 44, 55]

result = list(map(lambda x: x+5, nums))
print(result)

#Filter
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)

#Generadores
#are a type of iterable, like lists or tuples.Unlike lists, they don't allow indexing with arbitrary indices,
def countdown():
    i=5
    while i > 0:
        yield i #The yield statement is used to define a generator, replacing the return of a function to provide a result to its caller without destroying local variables.
        i -= 1

for i in countdown():
    print(i)

#Generadores de lsitas
def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))

#Decoradores: Decorators provide a way to modify functions using other functions.
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated()


#Decorador con Wrap
#Python provides support to wrap a function in a decorator by pre-pending the function definition with a decorator name and the @ symbol.
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

@decor
def print_text():
    print("Hello world!")

print_text();


#Recursion
#Recursion is a very important concept in functional programming.
#The fundamental part of recursion is self-reference - functions calling themselves.
def factorial(x):
    if x == 1:
        return 1 #The base case acts as the exit condition of the recursion.
    else:
        return x * factorial(x-1)

print(factorial(5))


#Sets
#They share some functionality with lists, such as the use of in to check whether they contain a particular item.
num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)
print("spam" not in word_set)

#Sets cannot contain duplicated elements
nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

#Sets con operacioens matematicas: conunjos
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)


#Itertools
from itertools import count

for i in count(3):
    print(i)
    if i >=11:
        break

#Itertools libreria accumulate & takewhile
from itertools import accumulate, takewhile

nums = list(accumulate(range(8))) #accumulate - returns a running total of values in an iterable.
print(nums)
print(list(takewhile(lambda x: x<= 6, nums))) #takewhile - takes items from an iterable while a predicate function remains true;

#Itertools: Permutaciones
from itertools import product, permutations

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))


#Ejercicio Permutaciones
from itertools import product
a={1, 2}
print(len(list(product(range(3), a)))) #6

#t is 6 because of following combinations (0,1)(1,1)(2,1) and (0,2) (1,2) (2,2) here it is (range,value) where range 0,1,2, and value is taken from num function that we provided 1,2
