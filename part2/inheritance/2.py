class Cal(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def add(self):
        return self.v1 + self.v2

    def sub(self):
        return self.v1 - self.v2

    # def multiply(self):
    #     return self.v1 * self.v2
    # def setV1(self, v):
    #     self.v1 = v
    # def getV1(self)
    #     return self.v1


class CalMulti(Cal): #상속된 class에 생성자가 없다면, 부모 class의 생성자를 참조하게 된다.
    def multiply(self):
        return self.v1 * self.v2

class Div(CalMulti): #상속된 class에 생성자가 없다면, 부모 class의 생성자를 참조하게 된다.
    def div(self):
        return self.v1 / self.v2


c1 = Div(10,10)
print (c1.add())
print (c1.sub())
print (c1.multiply())
print (c1.div())

