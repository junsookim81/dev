real_id = "junskim"
real_password = "20112415"


instr = input("please input your id \n")

if instr == real_id :
    instrpw = input("please input your password \n")
    if instrpw == real_password:
        print("welcome JS")
    else :
        print("check your password")
else:
    print("check your id")


    