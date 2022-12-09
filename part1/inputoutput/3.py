real_es = "20121219"
real_sh = "20160321"


instr = input("please input your birthday \n")
print(type(instr))

if instr == real_es :
    print("welcome ES")
else :
    if instr == real_sh:
        print("welcome sh")
    else :
        print("who are you")


if instr == real_es :
    print("welcome ES")
elif instr == real_sh:
    print("welcome sh")
else :
    print("who are you")