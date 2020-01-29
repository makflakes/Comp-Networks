import socket
import random
from ast import literal_eval

N = random.randint(25,100)

rando = []
for i in range(N):
    rando.append(random.randint(1,100))

print ('Type D for duplicates or I for intersection')
option = input()

s = socket.socket()
host = socket.gethostbyname('localhost')
portc = 5000
ports = 12345

s.bind((host,portc))

s.connect(('10.59.120.114',ports))

s.send(bytes(str(option), 'UTF-8'))   #options 

print("\n")

s.send(bytes(str(N), 'UTF-8'))   #size

print("\n")

print('\nCreated array: ',rando)
s.send(bytes(str(rando),'UTF-8'))   #array elements

print("\n")

#tmp = s.recv(N*1024).decode('utf-8')
#print(tmp)

#out = literal_eval(tmp)
#print('\nFiltered array: ',out)


temp2 = s.recv(N*1024).decode('utf-8')
intersection = literal_eval(temp2)
print('Requested Output: ',intersection)

print('hello')
s.close()