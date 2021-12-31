#Funcion sin argumentos
def my_func():
    print("spam")
    print("spam")
    print("spam")

my_func()


#Argumentos
def print_with_exclamation(word):
    print(word + "!")

print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")


#Funciones con variavles como argumentos
def function(variable):
    variable += 1
    print(variable)

function(7)
# print(variable) Function arguments can be used as variables inside the function definition. However, they cannot be referenced outside of the function's definition. This also applies to other variables created inside a function.

#Technically, parameters are the variables in a function definition, and arguments are the values put into parameters when functions are called.

#Funcion con 2 o más argumentos
def suma(x,y):
    return x+y;

suma(3,2);

#Funciones con Funciones como argumentos
def test(funcSuma, x, y):
    dobleSuma = funcSuma(x,y);
    
    return funcSuma(dobleSuma, dobleSuma);

suma(3,3);

respuesta = test(suma, 2,1); # functions are just like any other kind of value.
print(respuesta)

#Retorno de funciones
def max(x, y):
    if x >= y:
        return x
    else:
        return y


print(max(4, 7))
z = max(8, 5)
print(z)

#Despues del retorno
def add_numbers(x, y):
    total = x + y
    return total
    print("This won't be printed") #Once you return a value from a function, it immediately stops being executed. Any code after the return statement will never happen.

print(add_numbers(4, 5))

#Funciones como objetos
def multiply(x, y):
    return x * y

a = 4
b = 7
operation = multiply
print(operation(a, b)) # functions are just like any other kind of value.

#Funcioens como argumentos
def add(x, y):
    return x + y

def do_twice(func, x, y):
    return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b))