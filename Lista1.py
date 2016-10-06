#def Mayor(rango):
Lista = []
c = 0
while c < rango:
    num = eval(input("Numero {}: ".format(c+1)))
    Lista.insert(c,num)
    c = c + 1
#print (Lista)
mayor = 0
while mayor < rango:
    if (mayor < len(Lista)):
        print ("El mayor número de la lista es: ",max(Lista))
    mayor = mayor + rango
#rango = int(input("Ingrese el rango de la lista, por favor: "))
#Mayor(rango)


        
