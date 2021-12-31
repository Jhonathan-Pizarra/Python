#Excpeciones
#The following code produces the ZeroDivisionError exception by trying to divide 7 by 0.
num1 = 7
num2 = 0
#print(num1/num2)

#Capturar Errores
try:
    num1 = 7
    num2 = 0
    print (num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occurred")
    print("due to zero division")

#Capturas especificas
try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Error occurred")

#Capturas generales
try:
    word = "spam"
    print(word / 0)
except:
    print("An error occurred")

# Claúsula Finally
try:
    print("Hello")
    print(1 / 0)
except ZeroDivisionError:
    print("Divided by zero")
finally:
    print("This code will run no matter what")

#Levantar y personalizar error
name = "123"
raise NameError("Invalid name!")

#Capturar y levantar errores
try:
    num = 5 / 0
except:
    print("An error occurred")
    raise