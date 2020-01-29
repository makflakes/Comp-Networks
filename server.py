import socket
import random
from ast import literal_eval

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)         # Create a socket object
host = socket.gethostbyname('localhost') # Get local machine name
port = 12345
ports = 32451               # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

print ('host ip', host)
s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   #c.send(b'Thank you for connecting')
   
   a = c.recv(2).decode('utf-8') #options
   print(a)

   b = c.recv(1024).decode('utf-8')  #array size
   #print("\n")
   print(b)
   d = c.recv(1024).decode('utf-8')  # array elements
   #print(d)


   out = literal_eval(d)


   b=int(b)

   randomserverarray = []
   for i in range(b):
    randomserverarray.append(random.randint(1,100))

   print('Server Array is :', randomserverarray)

   


   lst3 = [value for value in randomserverarray if value in out]  

   seen = {}
   duplicates = []

   if a == 'D':
     for x in out:
          if x not in seen:
             seen[x]=1
     else:
          if seen[x]==1:
            duplicates.append(x)
          seen[x]+=1
   
   #print(lst3)

   #out = list(dict.fromkeys(out))
   temp = list(dict.fromkeys(out)) 
   #c.send(bytes(str(temp),'UTF-8'))

   if a == 'I':
       c.send(bytes(str(lst3),'UTF-8'))
   if a == 'D':
       c.send(bytes(str(temp),'UTF-8'))
  
  
   c.close() 