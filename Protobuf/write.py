import address_pb2



person = address_pb2.Person()



person.name = 'junsoo'

person.age = 42

person.email = 'juns@mycompany.com'



try:

 f = open('myaddress','wb')

 f.write(person.SerializeToString())

 f.close()

 print ('file is wriiten')

except IOError:

 print ('file creation error')