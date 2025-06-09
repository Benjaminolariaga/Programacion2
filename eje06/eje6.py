plata=0
mil1=0
mil2=0
dos1=0
dos2=0
total=0


print("cuanta plata queres sacar")
plata=int(input())

if(plata>999):

    mil1=plata%1000
    mil2=plata//1000
    dos1=mil1%200
    dos2=mil1//200


    print("sacas ",mil2," billetes de mil ","sacas ",dos2," billetes de docientos", " no pudimos sacar", dos1)
else:
    if(plata>199):
        dos1=plata%200
        dos2=plata//200
        print("sacas ",dos2," billetes de docientos"," no pudimos sacar ",dos1)
    else:
        print("1te caes amigo tan pobre sos")
