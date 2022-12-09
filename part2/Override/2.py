class Cal(object):
    _history = []
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def add(self):
        result = self.v1 + self.v2
        Cal._history.append("add : %d + %d = %d" %(self.v1, self.v2, result)) # + str(result)로 대체할 수도 있음
        return result
    def sub(self):
        result = self.v1 - self.v2
        Cal._history.append("sub : %d - %d = %d" %(self.v1, self.v2, result)) # + str(result)로 대체할 수도 있음
        return result
    def info(self):
        return "Cal => v1 : %d, v2 : %d" %(self.v1, self.v2)

class CalMultiply(Cal):
    def multiply(self):
        result = self.v1 * self.v2
        Cal._history.append("mul : %d * %d = %d" %(self.v1, self.v2, result)) # + str(result)로 대체할 수도 있음
        return result
    def info(self):
        #return super().info() 이렇게 하면 부모클래스의 info가 호출됨
        return "CalM => %s" % super().info()

class CalDiv(CalMultiply):
    def div(self):
        result = self.v1 / self.v2
        Cal._history.append("mul : %d / %d = %d" %(self.v1, self.v2, result)) # + str(result)로 대체할 수도 있음
        return result
    def info(self):
        return "CalD => %s" % super().info()

c0 = Cal(30,60)
print (c0.info())
c1 = CalMultiply(10,10)
print (c1.info())
c2 = CalDiv(10,5)
print (c2.info())