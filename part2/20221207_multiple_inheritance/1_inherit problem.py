



class C1():
    def c1_method(self):
        print ('c1_method')
    def m(self):
        print ("C1 m")

class C2(C1):
    def c2_method(self):
        print ('c2_method')
    def m(self):
        print ("C2 m")
        
class C3(C2):
    pass


a = C3()
# a.c1_method()
# a.c2_method()
a.m()