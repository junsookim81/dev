# # members = ['JS', 'ES', 'SH', 'RA', "tree"]
# # for i in range(0,3) : 
# #     print (members[i])

# j=0
# while j < len(members) : #이렇게 해야 배열이 길어져도 code를 수정할 필요가 없다.
#     print (members[j])
#     j = j+1


# members = ['JS', 'ES', 'SH', 'RA', "tree"]
# for i in members : #반복을 위해 필요한 code가 모두 "for in 문" 내에 들어있다. 대부분 언어가 while을 지원하는 한편 for in문은 그렇지 않다.
#     print (i)


i = [0,1,2,3,4,5]
for item in i:
    print('helloworld')


for item in [0,1,2,3,4,5]:
    print('helloworld oh!')


for item in range(95,100):
    print('helloworld oh! oh oh!!!'+str(item))

for item in range(9990, 10000):
    print('helloworld wow!!!'+str(item))