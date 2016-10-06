#Primera funcion
def Mayor(rango):
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
            print ("El número mayor de la lista es: ",max(Lista),"\n")
        mayor = mayor + rango
print("Primera funcion:\n")
rango = int(input("Ingrese el rango de la lista, por favor: "))
Mayor(rango)
rango1= int(input("Ingrese el rango de la lista, por favor: "))
Mayor(rango1)
rango2= int(input("Ingrese el rango de la lista, por favor: "))
Mayor(rango2)

#Segunda Funcion
def MindZero (a):
    c = 0
    print ("La lista es: ",a)
    while c < len(a):
        if a[c] < 0:
            a[c] = 0
        else:
            a[c] = a[c]
        c = c + 1
    print ("La nueva lista sin los negativos es: ", a,"\n")
print("Segunda funcion:\n")
a= int(input("Ingrese un número para la lista: "))
b= int(input("Ingrese un número para la lista: "))
c= int(input("Ingrese un número para la lista: "))
MindZero ([a, b, c])
d= int(input("Ingrese un número para la lista: "))
e= int(input("Ingrese un número para la lista: "))
f= int(input("Ingrese un número para la lista: "))
MindZero ([d, e, f])
g= int(input("Ingrese un número para la lista: "))
h= int(input("Ingrese un número para la lista: "))
i= int(input("Ingrese un número para la lista: "))
MindZero ([g, h, i])

#Tercera Funcion
def HyperDelete (List):
    i = 0
    print ("La lista es: ",List)
    while (i < len(List)):
        del List[i]
        i = i+ 1
    print ("La lista después de remover los números es: ",List,"\n")
print("Tercera funcion:\n")
a= int(input("Ingrese un número para la lista: "))
b= int(input("Ingrese un número para la lista: "))
c= int(input("Ingrese un número para la lista: "))
HyperDelete ([a, b, c])
d= int(input("Ingrese un número para la lista: "))
e= int(input("Ingrese un número para la lista: "))
f= int(input("Ingrese un número para la lista: "))
HyperDelete ([d, e, f])
h= int(input("Ingrese un número para la lista: "))
i= int(input("Ingrese un número para la lista: "))
j= int(input("Ingrese un número para la lista: "))
HyperDelete ([h, i, j])

































