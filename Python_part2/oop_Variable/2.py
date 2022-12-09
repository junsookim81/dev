class C:
    def __init__(self, v) :
        self.value = v+3
    # def show(self):
    #     print(self.value)

    def setValue(self, v) :
        self.value = v+5

    def getValue(self):
        return self.value


c1 = C(10)
print(c1.getValue())

c1.setValue(20)
print(c1.getValue())

#루비는 반드시 getValue, setValue를 써야 하는데, 파이선은 그렇지 않다.
#그렇다면 그럼에도 불구하고 get/set을 알아야 하는 이유는?????

