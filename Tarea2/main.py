def encontrar_superposicion_maxima(intervalos):
    n = len(intervalos)
    max_superposicion = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            # Verificar si hay superposición antes de calcular la intersección
            if intervalos[i][1] >= intervalos[j][0] and intervalos[j][1] >= intervalos[i][0]:
                interseccion = min(intervalos[i][1], intervalos[j][1]) - max(intervalos[i][0], intervalos[j][0]) + 1
                max_superposicion = max(max_superposicion, interseccion)

    return max_superposicion


def main():
    try:
        while True:
            n = int(input())
            intervalos = []
            con = 0

            for _ in range(n):
                try:
                    intervalos = []
                    j = input().split()
                    #print("aber weooooon0: ",j)
                    if (len(j)!=1):
                        for h in j:
                            x, y = map(int, j[:2])
                            intervalos.append([x,y])
                            j = j[2:]
                            #print("aber weooooon1: ",intervalos)
                        
                        #print("aber weooooon2: ",int(k))
                except ValueError:
                    #print("AAAAAAAAAAAA")
                    print("final: ",intervalos)
                    resultado = encontrar_superposicion_maxima( intervalos)
                    print("superposicion_maxima: ",resultado)
                    

    except EOFError:
        pass

if _name_ == "_main_":
    main()
