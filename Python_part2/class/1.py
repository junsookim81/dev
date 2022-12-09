
class cal(object):
    def __init__(self, x1, y1): #여기서 init은 생성자, 매개변수 self는 instance, 구체적으로는 instance를 객체라한다.
        self.x1 = x1 #여기서 self가 instance를 의미한다.
        self.y1 = y1
        
    def add(self):
        return(self.x1 + self.y1)
    def subtract(self):
        return(self.x1 - self.y1)
       

c1 = cal(10,10) #class의 호출하면, 위에 있는 cal class의 생성자가 생성이 된다. 그러니까 쉬운말로 하면 class를 호출할 때, 괄호안의 10,10을 instance로 하는 class가 생성된다는 이야기.
print(c1.add()) #add 는 method
print(c1.subtract())

c2 = cal(30,20) #마찬가지로 여기서는 30,20을 매개변수로 하는 cal이 생성된다.
print(c2.add())
print(c2.subtract())

