members = ['JS', 'ES', 'SH', 'RA', "tree"]
for i in range(0,3) : 
    print (members[i])

j=0
while j < len(members) : #이렇게 해야 배열이 길어져도 code를 수정할 필요가 없다.
    print (members[j])
    j = j+1
