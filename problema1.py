def obtenerInput():
    input = [[1, 2, 3], [4, 5, 6], [1,5,4]]
    return input

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

def f(i):
    cajaf = R[i]
    h,a,b = cajaf
    posibles = [0]

    for j in range(0,i):
        _,a2,b2 = R[j]
        if(a2>a and b2>b): #if caja j mas grande que caja i
            posibles.append(f(j))

    return h+max(posibles)


L = obtenerInput()
R = generarRotaciones(L)
ordenarLados(R)
print(R)
R.sort(key=areaCaja,reverse=1)
print(R)
f1 = []
for i in range(0,len(R)):
    f1.append(f(i))
print(f1)
print("la altura maxima que se puede obtener con estas cajas es de:",max(f1))

