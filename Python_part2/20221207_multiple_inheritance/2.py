

class CalMulti(): #상속된 class에 생성자가 없다면, 부모 class의 생성자를 참조하게 된다.
    def multiply(self):
        return self.v1 * self.v2

class Div(): #상속된 class에 생성자가 없다면, 부모 class의 생성자를 참조하게 된다.
    def div(self):
        return self.v1 / self.v2

class Cal(CalMulti, Div):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def add(self):
        return self.v1 + self.v2

    def sub(self):
        return self.v1 - self.v2

C = Cal(100,10)
print (C.add())
print (C.sub())
print (C.multiply())
print (C.div())
