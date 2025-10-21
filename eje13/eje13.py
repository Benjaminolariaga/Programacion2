multiprin=1
sumaprin=0
multicont=1
sumacont=0
m=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

for x in range(4):
    for i in range(4):
        print(m[x][i])
        if (x==i):
            sumaprin=sumaprin+m[x][i]
            multiprin=multiprin*m[x][i]
        elif(i==len(m)-1-x):
            sumacont=sumacont+m[x][i]
            multicont=multicont*m[x][i]
            
            
            
print("la suma de la diagonal principal es:",sumaprin,"la multiplicacion de la diagonal principal es:",multiprin,"la suma de la dagional coontraria es:",sumacont,"la multiplicacion de la diagonal contraria es:",multicont)
            

            