def MindZero (List):
    i = 0
    print ("La lista es: ",List)
    while (i < len(List)):
        del List[i]
        print("Se eliminó el elemento",List[i],"con índice", i)
        i = i+ 1
    print ("La lista después de remover los números es: ",List)

MindZero ([5, -13, 10, -8, -6, 1])
