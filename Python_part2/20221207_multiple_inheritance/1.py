class C1():
    def c1_method(self):
        print ('c1_method')
    def m(self): #다중상속시 2개의 class에 모두 같은 m method가 정의 되어 있다면 상속받은 C3 class에서 먼저 호출되는 class의 method가 사용된다.그런데 이 문제는 다중상속에서만 발생하는것은 아닌것 같다.
        print ("C1 m")

class C2():
    def c2_method(self):
        print ('c2_method')
    def m(self):
        print ("C2 m")

class C3(C1, C2):
    def m(self):
        print ("C3 m")
    pass


a = C3()
a.c1_method()
a.c2_method()
a.m()