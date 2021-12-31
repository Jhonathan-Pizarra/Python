def function(named_arg, *args):
    print(named_arg)
    print(args)

function(1, 2, 3, 4, 5)

#Valores por defecto
def function(x, y, food="spam"):
    print(food)

function(1, 2)
function(3, 4, "egg")

#------------------------------
#Kwargs
def my_func(x, y=7, *args, **kwargs):
    print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)

#The keyword arguments return a dictionary in which the keys are the argument names, and the values are the argument values
#a and b are the names of the arguments that we passed to the function call.
#The arguments returned by **kwargs are not included in *args.

#------------------------------

#Tuple Unpacking
numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)

#A variable that is prefaced with an asterisk (*) takes all values from the iterable that are left over from the other variables:
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)


#Operador ternario
a = 7
b = 1 if a >= 5 else 42
print(b)

status  = 1
msg = "Logout" if status == 1 else "Login"
print(msg)

#Else en bucles (For o WHile)
for i in range(10):
    if i == 999:
        break
else:
    print("Unbroken 1")

for i in range(10):
    if i == 5:
        break
else:
    print("Unbroken 2")


for i in range(10):
   if i > 5:
      print(i) #6 y muere el programa
      break
else:
   print("7")

#Else Exceptions
try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)

try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)


#Imported and scripted
def function():
    print("This is a module function")

if __name__=="__main__": #This ensures that it won't be run if the file is imported.
    print("This is a script")

#When the Python interpreter reads a source file, it executes all of the code it finds in the file. Before executing the code, it defines a few special variables.
#For example, if the Python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value "__main__". If this file is being imported from another module, __name__ will be set to the module's name.
