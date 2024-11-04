import os
os.system('cls')
conjunto={'zagalo':'57','Omaida':'58'}
nombre='pepe'
edad='40'
sexo='0'
conjunto[nombre]=edad  #agregar elementos a un conjunto
for nombre, edad in conjunto.items():
   print('Nombre ', nombre ,' Edad ', edad )
evento_1=[(1,1),(1,2),(1,3)]
evento_1=[(6,1),(6,2),(6,3)]
print(evento_1)
evento_1.append((3,3))
print(evento_1[0])
print(evento_1)
evento_3=[('cara','cara'),('cara','sello')]
print(evento_3)