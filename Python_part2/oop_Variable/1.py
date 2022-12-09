class C:
    def __init__(self, v) :
        self.value = v
    def show(self):
        print(self.value)

c1 = C(5) #C class를 호출하자, C class에 매개변수값이 10인 class의 복사본이 생성된다.
# print(c1.value)
# c1.value = 20
# print (c1.value)
c1.show()

