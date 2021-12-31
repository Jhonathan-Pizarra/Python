#Temas:
# Listas o arreglos
# Listas vacias
# lisotas anidadas (matrices)
# listas y cadenas

#arreglos
words = ["Hello", "world", "!"]

#lista vacia
vacia = [];
print(vacia);

#Listas
numero = 3;
arreglo = ["cadena", 0, [1,2,numero], 4.56];
print(arreglo[0]);
print(arreglo[1]);
print(arreglo[2][2]);

#matrices
matriz = [
    [1,2,3],
    [2,5,6],
    [7,8,9]
];

print(matriz[1][2]);

#listas y cadenas
cadena = "Hola Mundo!";
print(cadena[6]); #M
#! el espacio "" también es un simbolo y tiene un índice.
# ademas, el accder a un elemento digamos 35 producira un error puesto que no existe
