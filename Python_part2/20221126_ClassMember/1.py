class Cs:
    @staticmethod #class에 소속임을 명시(장식자라 부름)
    def static_method():
        print("Static method")
    @classmethod #class에 소속임을 명시(장식자라 부름)
    def class_method(cls): #class method는 첫번째 인자(cls)가 self처럼 꼭 있어야 한다. 이름을 self라고 하든 cls라고 하든 관계없음.
        print("Class method")
    def instance_method(self): #instance method에는 첫번째 인자(self) 필요,
        print("Instance method")

i = Cs() #instance 생성
Cs.static_method() #class member에 2가지 종류가 있음, static method 와 class method.
Cs.class_method() #class method
i.instance_method() #instance method, instance method는 변수값을 전달, instance method는 class를 따로 부르지 않아도 실행됨.