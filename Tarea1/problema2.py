import time
def obtenerInput():
    #input = [[1, 2, 3], [4, 5, 6], [1,5,4]]
    listaGod = []
    n = int(input())
    while n != 'EOF':
        lista = []
        n = int(n)
        for _ in range(0,n):
            cajita = input().strip().split(' ')
            lista.append([int(cajita[0]),int(cajita[1]),int(cajita[2])])
        listaGod.append(lista)
        try: n = input()
        except: n  = 'EOF'
    return listaGod

def obtenerInput2():
    lista = []
    n = int(input())
    for _ in range(0,n):
            cajita = input().strip().split(' ')
            lista.append([int(cajita[0]),int(cajita[1]),int(cajita[2])])
    return lista

def generarRotaciones(lista): # añadir las instancias posibles de las cajas
    listaExt = []
    i = 0
    for caja in lista:
        while i<3:
            listaExt.append([caja[(i+0)%3],caja[(i+1)%3],caja[(i+2)%3]])
            i+=1
        i = 0 
    return listaExt

def ordenarLados(lista): #dejar las cajas como: altrura, lado grande, lado chico
    for caja in lista:
        if (caja[1] < caja[2]):
            tmp = caja[1]
            caja[1] = caja[2]
            caja[2] = tmp

def areaCaja(caja): #area basal de la caja para poder ordenarlas
    return caja[1]*caja[2]


def main():
    superL = obtenerInput()
    for L in superL:
        R = generarRotaciones(L)
        ordenarLados(R)
        R.sort(key=areaCaja,reverse=1)
        F = []
        for i in range(0,len(R)):
            h,a,b = R[i]
            posibles = [h]
            for j in range(0,i):
                if(R[j][1]>a and R[j][2]>b): #if caja j mas grande que caja i
                    posibles.append(h+F[j])
            F.append(max(posibles))
        print(max(F))

def main2():
    L = obtenerInput()
    R = generarRotaciones(L)
    ordenarLados(R)
    R.sort(key=areaCaja,reverse=1)
    F = []
    for i in range(0,len(R)):
        h,a,b = R[i]
        posibles = [h]
        for j in range(0,i):
            if(R[j][1]>a and R[j][2]>b): #if caja j mas grande que caja i
                posibles.append(h+F[j])
        F.append(max(posibles))
    print("la altura maxima que se puede obtener con estas cajas es de:",max(f1))

inicio = time.time()
main()
final = time.time()
print("tiempito:",(final-inicio)*1000,'ms')