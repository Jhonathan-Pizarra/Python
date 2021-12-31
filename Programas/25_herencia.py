#Herencia
'''
Inheritance provides a way to share functionality between classes.
Imagine several classes, Cat, Dog, Rabbit and so on. Although they may differ in some ways
they are likely to be similar in others
This similarity can be expressed by making them all inherit from a superclass Animal, which contains the shared functionality.
'''
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Cat(Animal): #La superclase va entre paréntesis
    def purr(self):
        print("Purr...")


class Dog(Animal):
    def bark(self):
        print("Woof!")


fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()

'''
A class that inherits from another class is called a subclass.
A class that is inherited from is called a superclass.

If a class inherits from another with the same attributes or methods, it overrides them.
'''

#Herencia indirecta
#Una clase que hereda de otra que también hereda
class A:
    def method(self):
        print("A method")


class B(A):
    def another_method(self):
        print("B method")


class C(B):
    def third_method(self):
        print("C method")


c = C()
c.method()
c.another_method()
c.third_method()

#Cláusula Super
class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()