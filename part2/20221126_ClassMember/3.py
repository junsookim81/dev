class Cs:
    count = 0 #파이썬 규친인데, 클래스의 안, 매소드의 밖(현재위치)에 변수를 정의하면 class에 소속된 변수가 됨.
    def __init__(self):
        Cs.count = Cs.count + 1
    @classmethod
    def getCount(cls):
        return Cs.count

i1 = Cs() #Cs라는 class를 instance화 시킴
i2 = Cs()
i3 = Cs()
i4 = Cs()
print (Cs.getCount())