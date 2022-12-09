

def login(x, y) :
    for input in y :
        if x == input :
            return('welcome')
    return('who are you')

members=['es', 'js', 'sh', 'ra']
uid = input("please input uid : \n")
print(login(uid, members))

