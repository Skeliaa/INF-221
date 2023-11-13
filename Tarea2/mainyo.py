#print(input()) prueba loca

def obtenerInput():
    #input = [[1, 2], [4, 6], [1,6]]
    inputLista = []
    n = int(input())
    while n != 'EOF':
        lista = []
        n = int(n)
        arreglos = input().strip().split(' ')
        i=0
        for _ in range(0,n):
            lista.append([int(arreglos[i]),int(arreglos[i+1])])
            i+=2
        inputLista.append(lista)
        try: n = input()
        except: n  = 'EOF'

    return inputLista


def main():
    L = obtenerInput()
    print(L)
    for A in L:
        1
