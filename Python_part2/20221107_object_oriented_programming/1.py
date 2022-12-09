#object는 class와 instance로 구성되어 있다.

#class 그룹,분류 instance 사례

# class 역시 모듈처럼 수납공간이라고 볼 수 있는데, 모듈과는 다르게 class는 함수(logic) 뿐 아니라 변수(data)도 grouping한것
# class를 그냥쓰는 경우는 거의 없고, 이것들을 복제해서 여기저기 사용하는데 그것들이 instance!
    # 포유류를 만들어 놓으면 사람 고양이 개 기능을 복제해서 쉽게 만들어 낼 수 있다.

# instance는 class와는 다른 값의 변수를 가지게 되는데, 이 다른 값으로 동일한 함수를 이용해 계산을 한다

# class a
# class a, instance1, 변수x, 함수1
# class a, instance2, 변수y, 함수2
# class a, instance3, 변수z, 함수3

name = 'junsoo' #여기서 junsoo 라는 문자열이 객체
#junsoo라는 값을 가지고 있는 객체가 생성된코드임.
#이것을 길게 풀어쓰면 아래와 같은데, 
name = str('junsoo?') #여기서 str이 class, str('junsoo?')가 instance, ==> class와 instaqnce가 있으니 객체가 된다.  이거 function 쓰는것과 뭐가 다르지..?
name2 = str('es?') #여기서 str이 복제된 class, str('es?')가 instance 

#name,name2라는 instance가 각각 생성되었고 name에는 junsoo가 name2는 es가 저장되어 있음.

print (name.upper()) #str:클래스, upper():함수 다른말로 methods 함수==method==function, name:instance

names = []
names.append('jun')
names.append('es')
print(names)
