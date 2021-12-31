#Sectores
#List slices provide a more advanced way of retrieving values from a list.
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6]) #4,9,16,25
print(squares[3:8]) #9 al 49
print(squares[0:1]) # 0

#De principio a fin y viceversa
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7]) ##If the first number in a slice is omitted, it is taken to be the start of the list
print(squares[7:]) #If the second number is omitted, it is taken to be the end.

#Con saltos
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2]) #Del primero al último de 2 en 2
print(squares[2:8:3]) #Del 2 al 7 de 3 en e

#Sectores Negativos
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1]) #Del 1 al 64