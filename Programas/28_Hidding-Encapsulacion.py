class Spam:
    __egg = 7 # can't be accessed from outside the class.
    def print_egg(self):
        print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)
print(s.__egg)