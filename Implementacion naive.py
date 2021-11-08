#Implementacion naive

#Primero se piden el n y el m
n=int(input('n? '))
m=int(input('m? '))

#buenArregloSubi calcula todos los buenos arreglos de tamaño n acotados por m que parten en i
def buenArregloSubi(i,n,m):
    if i==0 or i==m+1: #Si i es 0 o mayor que m
        return 0 #No hay arreglos que parten con este numero
    if n==1 and i>=1 and i<=m: 
        return 1 #Solo existe 1 buen arreglo de tamaño 1 que parte en i, el arreglo compuesto por i
    else: #Para tamaños mayores que uno
        return buenArregloSubi(i-1,n-1,m) + buenArregloSubi(i,n-1,m) + buenArregloSubi(i+1,n-1,m) 
        #Se considera la suma de los buenos arreglos que partían en i-1, i e i+1 para n más grandes (o más pequeños, ya que la función los computa de arriba hacia abajo)

#conjuntoDeArreglos calcula la cantidad de buenos arreglos que hay en el conjunto A sub n,m
def conjuntoDeArreglos(n,m):
    suma=0 #Variable auxiliar para contener la suma
    for i in range(1,m+1): #Desde i=1 hasta i=m
        suma=suma + buenArregloSubi(i,n,m) #Sumar los buenos arreglos de tamaño n que parten i
    return suma

print(conjuntoDeArreglos(n,m))
