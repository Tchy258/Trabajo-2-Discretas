#Implementacion ligeramente más eficiente que evita recalcular valores
import numpy as np

#Primero se piden el n y el m
n=int(input('n? '))
m=int(input('m? '))

#buenosArreglos calcula todos los buenos arreglos de tamaño n acotados por m
def buenosArreglos(n,m):
  cantidades=np.zeros((m+2,n),dtype=int) #Se crea una matriz de ceros de m+2 por n para almacenar las cantidades de buenos arreglos
  for i in range(1,m+1): #Para i desde 1 hasta m
    cantidades[i][0]=1 #En n=0, hay 1 arreglo para todo i entre 1 y m
  for j in range(1,n): #Para j desde 1 hasta n-1
    for i in range(1,m+1): #Para i desde 1 hasta m
      cantidades[i][j]=cantidades[i-1][j-1] + cantidades[i][j-1] + cantidades[i+1][j-1]
      #La cantidad de arreglos que parten en i de tamaño j será la suma de los arreglos que
      #partían en i-1, i e i+1 de tamaño j-1
      #Para i=0 o i=m+1 el valor por defecto siempre es 0
  suma=0 #Variable auxiliar para alojar la suma de todos los arreglos de tamaño n acotados por m
  for i in range(1,m+1): #Para i desde i hasta m
    suma=suma + cantidades[i][n-1] #Sumar todos los arreglos de tamaño n (ya que partían desde 0)
  return suma

print(buenosArreglos(n,m))
