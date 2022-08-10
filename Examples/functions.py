from pickle import GLOBAL


PI = 3.14

class Rectangle:
    def __init__(self, a:int = 1, b:int = 1):
        "Pravougaonik"
        self.__a = a 
        self.__b = b
        self.__o = 2 * (a + b)

    def setA(self, a:int):
        self.__a = a
        return self

    def setB(self, b:int):
        self.__b = b
        return self

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b
    
    def getPerimeter(self):
        "Vraća površinu pravougaonika"
        return self.__o

class Square(Rectangle):
    def __init__(self, a:int = 1):
        "Kvadrat"
        Rectangle.__init__(self, a, a) #super().__init(self, a, a)

    #

    def getInscribedCircleArea(self):
        "Vraca povrsinu upisanog kruga"
        global PI
        return PI * ((Rectangle.getA(self) / 2) ** 2)

sq = Square(5)

print(sq.getInscribedCircleArea())

sq.setA(3).setB(2)

print(sq.getInscribedCircleArea())
print(sq.getB())