class C:
    def __init__(self, v) :
        self.__value = v
    def show(self):
        #print(self.__value) #underbar 2개는 외부에서 내부변수의 접근을 막기위한 방법으로 쓰인다.
        return self.__value*10

c1 = C(10)
#print(c1.__value) #밖에서는 __value를 읽거나 쓸 수는 없다.
print(c1.show())
