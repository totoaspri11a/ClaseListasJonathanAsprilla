def MindZero (a):
    c = 0
    print ("La lista es: ",a)
    while c < len(a):
        if a[c] < 0:
            a[c] = 0
        else:
            a[c] = a[c]
        c = c + 1
    print ("La nueva lista sin los negativos es: ", a)

MindZero ([5, -13, 10, -8, -6, 1])
