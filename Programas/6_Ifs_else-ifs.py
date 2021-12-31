#Temas:
# ifs
# ifs anidados
# if-else
# if-else anidados
# else if


#Ifs
if (1 > 2): #(1 > 2 es una expresión que resulta en true or false)
    print("Dentro del if");
print("Fuera del if");

#También puede que evalue 2 o más expresiones, esto con operadores lógicos
grade = 88
if(grade >= 70 and grade <= 100):
    print("Passed!");

#Ifs anidados
if ("falso" == "falso"): #(1 > 2 es una expresión que resulta en true or false)
    print("Nivel 1");
    if("verdad" == "verdad"):
        print("Nivel 2");

#If-else
x = 3;
if(x==5):
    print("Yes");
else:
    print("No");

#If-else anidados
x = 5;
if(x==6):
    print("Yes");
else:
    if (x == 7):
        print("Yes, is 7");
    else:
        if (x == 5):
            print("Yes, is 5");
        else:
            print("No");


#Else if
x = 7;
if (x==5):
    print("5");
elif (x==6):
    print("6");
elif (x==4):
    print("4");
else:
    print("No es ningún numero entonces");

