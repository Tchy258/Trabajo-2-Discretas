#Implementacion aún más eficiente que evita recalcular valores
import numpy as np

#Primero se piden el n y el m
n=int(input('n? '))
m=int(input('m? '))

#buenosArreglos calcula todos los buenos arreglos de tamaño n acotados por m
def buenosArreglos(n,m):
    if m==1: return 1
    if m==2: return 2**n
    cantidades=np.zeros((m+2,n),dtype=int) #Se crea una matriz de ceros de m+1 por n para almacenar las cantidades de buenos arreglos
    if m%2==0: #Si m es par
        for i in range(1,int(m/2)+1): #Para i desde 1 hasta m/2 +1
            cantidades[i][0]=1 #En n=0, hay 1 arreglo para todo i entre 1 y m
            cantidades[m+1-i][0]=cantidades[i][0]
        for j in range(1,n): #Para j desde 1 hasta n-1
            for i in range(1,int(m/2)+1): #Para i desde 1 hasta m/2
                cantidades[i][j]=cantidades[i-1][j-1] + cantidades[i][j-1] + cantidades[i+1][j-1]
                cantidades[m+1-i][j]=cantidades[i][j]
                #La cantidad de arreglos que parten en i de tamaño j será la suma de los arreglos que
                #partían en i-1, i e i+1 de tamaño j-1
                #Para i=0 o i=m+1 el valor por defecto siempre es 0
                #Ademas, estas cantidades estan espejadas a partir de m/2
        suma=0 #Variable auxiliar para alojar la suma de todos los arreglos de tamaño n acotados por m
        for i in range(1,int(m/2)+1): #Para i desde 1 hasta m/2
            suma=suma + 2*cantidades[i][n-1] #Sumar el doble de todos los arreglos de tamaño n (ya que partían desde 0)
    else: #m es impar
        for i in range(1,int((m/2)+1)): #Para i desde 1 hasta m/2
            cantidades[i][0]=1 #En n=0, hay 1 arreglo para todo i entre 1 y m/2, para el resto de i, se repite como espejo
            cantidades[m+1-i][0]=1
        cantidades[int(m/2)+1][0]=1 #El que falta
        suma=0 #Variable auxiliar para alojar la suma de todos los arreglos de tamaño n acotados por m
        for j in range(1,n): #Para j desde 1 hasta n-1
            for i in range(1,int((m/2)+2)): #Para i desde 1 hasta m/2 +1
                cantidades[i][j]=cantidades[i-1][j-1] + cantidades[i][j-1] + cantidades[i+1][j-1]
                cantidades[m+1-i][j]=cantidades[i][j]
                #La cantidad de arreglos que parten en i de tamaño j será la suma de los arreglos que
                #partían en i-1, i e i+1 de tamaño j-1
                #Para i=0 o i=(m/2)+2 el valor por defecto siempre es 0
            cantidades[int(m/2)+1][j]=cantidades[int(m/2)][j-1] + cantidades[int(m/2)+1][j-1] + cantidades[int(m/2)+2][j-1]
            #A diferencia del caso m par, este valor en particular no está espejado
        for i in range(1,int(m/2)+1): #Para i desde i hasta m
            suma=suma + 2*cantidades[i][n-1] #Sumar el doble de todos los arreglos de tamaño n (ya que partían desde 0)
        suma=suma + cantidades[int(m/2)+1][n-1] #Sumar los arreglos que parten en m/2 +1 (son únicos en el sentido de que no estan espejados)
    return suma

print(buenosArreglos(n,m))
