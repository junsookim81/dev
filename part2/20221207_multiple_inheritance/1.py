class C1():
    def c1_method(self):
        print ('c1_method')
class C2():
    def c2_method(self):
        print ('c2_method')
class C3(C1, C2):
    pass


a = C3()
a.c1_method()
a.c2_method()