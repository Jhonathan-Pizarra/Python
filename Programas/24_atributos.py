class Dog:
    #Classes can also have class attributes, created by assigning variables within the body of the class.
    legs = 4
    def __init__(self, name, color):
        self.name = name
        self.color = color

fido = Dog("Fido", "brown")
print(fido.legs)
print(Dog.legs)
#These can be accessed either from instances of the class, or the class itself.
#Class attributes are shared by all instances of the class.


#Atribute error
#Trying to access an attribute of an instance that isn't defined causes an AttributeError
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

rect = Rectangle(7, 8)
print(rect.color)


