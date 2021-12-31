#Metodos
class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    #Remember, that all methods must have self as their first parameter
    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.name) #These methods are accessed using the same dot syntax as attributes.
fido.bark()