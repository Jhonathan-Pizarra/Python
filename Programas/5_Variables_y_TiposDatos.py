#Temas:
# variables y tipos de datos
# concatenación
# castings
# type para saber el tipo de dato
# borrar variables
# operadores de asignacion
# operadores de incremento
# operadores lógicos

#Variables
x = 7;
y = "ocho";
z = 'A';
boleano = True; #no true
#Python determina automaticamente el tipo de dato que corresponde a la variable
x = "Siete"; #la variable se reemplaza de su valor y se coloca este nuevo

#Concatenacion
print("Jhonathan" +" " +"Pizarra");
print("cadena 1"+','+'cadena 2'); #no importa si es '' o ""
print("2"+"2");
#print("2"+2); #No se puede concaternar numeros y srtings

#Cadenas repetidas:
print("Oye, " * 3 + "Oye!"); #Si multiplicas por cero esa cadena "Oye," se pierde!

#Castings o conversiones
print("3" + "4") #Cadena: 34
print(int("3"+"4")) #Numero: 34

numero = int(input("Esribe un numero(entero): ")); #Si escribes algo que no sea un numero entero te dará error!
numero2 = float(input("Escribe otro nummero(decimal): "));

suma = numero + numero2

print(suma); #suma como numero
print(str(suma) + "... no es genial? :D"); #suma como cadena

test= float("210" * int(input("Enter a number:" ))) #"210" is a string × input of 2 = 210210 then converted to float= 210210.0
print(test);

print(type(float(2)));
print(type(float("2")));

#Borrar una variable
del test #booramos la variable test!
print(test) #y como la borramos no habrá una variable test a la que se haga referencia, producirá un error!

#Operadores de assignacion
x = 3
x *= 4 # es como decir x = 3 * 4 = 12

y = "spam"
y += "eggs"# pasa igual que con los numeros, solo que se concatena: spameggs

#Operadores de comparación
# <
# >
# <=
# >=
# !=
# ==
print( 2 == 3);
print("Hola" == "Hola");

#Operadores lógicos
# not
# and
# or
# in
# not in
# is
# is not
print( 1==1 and 2==2); #true
print( 1==1 or 2==2); #true
print( not 1==1); #false

#IMPORTANTE
#python no tiene operadores de incremento o decremento: x++, x--... lo que si tiene es esa forma: x +=1 que sería lo mismo
#ver teoría->operadores para concer más sobre operadores