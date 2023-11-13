from time import time
from random import randint
from generate import generar
def intersection(a,b):
    return min(a[1], b[1]) - max(a[0], b[0]) + 1

def conquer(arr):
    max = 0
    i = 0
    while i < len(arr) - 1:
        j = i + 1
        ls = []
        while (j < len(arr)) and (arr[i][1] > arr[j][0]):
            if(arr[j][1]-arr[j][0] > max):
                ls.append(arr[j])
            j += 1
        #print(ls)
        candidate = divide(arr[i], ls)
        #print(candidate)
        if(candidate > max):
            max = candidate
        i += 1
    return max

def divide(tuple, ls):
    localMax = 0
    for t in ls:
        tmp = intersection(tuple, t)
        if( tmp > localMax):
            localMax = tmp
    return localMax


def getData():
    bigArr = []
    flag = True
    n = int(input())

    while(flag):
        arr = []
        
        tuplas = input()
        tuplas = tuplas.split(' ')

        for i in range(0,2*n,2):
            aux = []
            for j in range(i,i+2):
                aux.append(int(tuplas[j]))
            arr.append(aux)

        bigArr.append(arr)
        try: n = int(input())
        except: flag = False

    return bigArr

def main():
    arr = getData()
    for elem in arr:
        #print(elem)
        
        print(conquer(elem))

def prueba(funcion,n): #tiempo que demora para input de largo n en [ms] 
    generar(n)
    start = time()
    funcion()
    end = time()
    
    return str((end-start)*1000).replace(".",",")


""" inicio = time()
main()
fin = time()
print(f"Tiempo: {(fin-inicio)*1000}" ) """
f1 = open("datos.csv","a")
n = randint(10**5,10**6)
f1.write(str(n)+";"+str(prueba(main,n))+"\n")
f1.close()
