"""
Programa para contar funciones sobreyectivas e inyectivas
Matematica discreta
Programado por: Montserrat Gil
Fecha 8/05/2022
"""

def conseguirFuncion(num,x,y):
    numero=""
    while num>0:
        res=num%y
        numero=str(res)+numero
        num=int(num/y)
    while len(numero)<x:
        numero="0"+numero
    return numero

def sobreyectivas(x,y,imprimir):
    contar=0
    for i in range(y**x):
        contiene=0
        funcion=conseguirFuncion(i,x,y)
        for l in range(y):
            if str(l) in funcion:
                contiene+=1
        if contiene==y:
            contar+=1
            if imprimir:
                print(funcion)
    return contar

def inyectivas(x,y,imprimir):
    contar=0
    for i in range(y**x):
        es=True
        funcion=conseguirFuncion(i,x,y)
        for l in range(y):
            temp=funcion
            temp=temp.replace(str(l),"")
            if len(temp)==(x-1):
                es=True
            elif len(temp)==x:
                es=True
            else:
                es=False
                break
        if es:
            contar+=1
            if imprimir:
                print(funcion)
    return contar


seguir=False
while not seguir:
    try:    
        dominio=int(input("Ingrese la cardinalidad del dominio de la funcion: "))
        contradominio=int(input("Ingrese la cardinalidad del contradominio de la funcion (1-10): "))
        seguir=True
    except:
        print("Ingrese numeros enteros")

seguir2=False
while not seguir2:
    imprimir=input("Desea imprimir las funciones? (ingrese si o no): ")
    
    if imprimir=="si":
        seguir2=True
        imprimir=True
    elif imprimir=="no":
        seguir2=True
        imprimir=False
    else:
        print("Ingrese si o no")

if imprimir:
    if not dominio<contradominio:
        print("Funciones sobreyectivas: ")
sobre=sobreyectivas(dominio,contradominio,imprimir)

if imprimir:
    if not contradominio<dominio:
        print("Funciones inyectivas: ")
iny=inyectivas(dominio,contradominio,imprimir)
    
print("El numero de funciones sobreyectivas es " + str(sobre))
print("El numero de funciones inyectivas es " + str(iny))