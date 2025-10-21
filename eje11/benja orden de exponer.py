import random
alist=["lautaro","benja","joaquin","theo","santino"]
orden=random.sample(range(1,6),5)

for x in range(0,5):
    print("el alumno ",alist[x],"va a pasar a exponer ",orden[x],"°")