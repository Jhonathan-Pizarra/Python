
def suma(x,y):
    return x+y;

def test(funcSuma, x, y):
    dobleSuma = funcSuma(x,y);
    
    return funcSuma(dobleSuma, dobleSuma);

suma(3,2);

respuesta = test(suma, 2,1);
print(respuesta)