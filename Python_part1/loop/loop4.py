in_string = input("please input : ")
loginstatus = False
members=['es', 'js', 'sh', 'ra']
for input in members :
    if in_string == input :
        print("welcome")
        loginstatus = True
if loginstatus == False :
    print("who are you")

#아래있는 코드는 list가 길어질수록 조건문이 계속 늘어나는 반면 위에 있는 코드는 list에 id만 추가하면 끝나게 된다.

# if instr == real_es :
#     print("welcome ES")
# elif instr == real_sh:
#     print("welcome sh")
# else :
#     print("who are you")