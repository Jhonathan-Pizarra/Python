#Asercion (Afirmacion) An expression is tested, and if the result comes up false, an exception is raised.
print(1)
assert 2 + 2 == 4
print(2)
assert 1 + 1 == 3
print(3)

#Asercion con 2 parámetros (Mensaje personalizdo)
temp = -10
assert (temp >= 0), "Colder than absolute zero!"