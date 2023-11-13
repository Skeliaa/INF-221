from random import randint
MAX = 100000000
N = 10**6

def generar(n):
    minA = -MAX
    maxA = -MAX-1
    f1 = open("inputmiau.txt","w")
    f1.write(str(n)+"\n")
    s=""
    for i in range(n):
        #if(i== 10**3 or i == 10**4 or i == 10**5):
            #print("tiktoking")
        #if(i== 10**6/5 or i== 2*10**6/5 or i== 3*10**6/5 or i== 4*10**6/5):
            #print("casicasi")
        minA = randint(minA,minA+1000)
        maxA = randint(minA,minA+10000)
        while minA>=maxA:
            minA = randint(minA,minA+1000)
            maxA = randint(minA,minA+10000)
        pattern = "{} {} "
        f1.write(pattern.format(minA,maxA))
    f1.close()
    print("listillo")