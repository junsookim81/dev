
import auth #auth라는 모듈을 import했다, 지금 auth라는 모듈에는 login이라는 함수 하나만 있지만 이와 유사한 기능의 함수가 한 100개 정도 auth라는 모듈이 들어있고 그중에 사용하고싶은것을 꺼내 쓴다고 생각해야 module에 대한 정의를 잘 이해한 것이다.

members=['es', 'js', 'sh', 'ra']
uid = input("please input uid : \n")
print(auth.login(uid, members))

