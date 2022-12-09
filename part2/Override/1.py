#Override : 부모객체가 가지고 있는 method를 자식객체(class)가 새롭게 다시 정의 하는것.

class C1:
    def m(self):
        return 'parent'

class C2(C1):
    
    def m(self):
        a = super().m()
        return  a + ' child'

output1 = C1()
output2 = C2()
print(output1.m())
print(output2.m())