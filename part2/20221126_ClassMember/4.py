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
    def multiply(self):
        result = self.v1 * self.v2
        Cal._history.append("mul : %d * %d = %d" %(self.v1, self.v2, result)) # + str(result)로 대체할 수도 있음
        return result
    def div(self):
        result = self.v1 / self.v2
        Cal._history.append("mul : %d / %d = %d" %(self.v1, self.v2, result)) # + str(result)로 대체할 수도 있음
        return result

    @staticmethod
    def history():
        for i in Cal._history:
            print(i)


c1 = Cal(10,10)
c1.add()
c1.add()
c1.add()
c1.multiply()
c1.add()
# print (c1.add())
# print (c1.sub())
# print (c1.add())
# print (c1.div())
# print (c1.multiply())

Cal.history()
