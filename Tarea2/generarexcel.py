from DivideAndConquer import main
from mainLongdickj import main2
from generate import generar
from time import time
from random import randint



f1 = open("datos.csv","a")
n = randint(10,100)
f1.write(str(n)+";"+str(prueba(main,n))+"\n")
f1.close
