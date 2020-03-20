import random

# Divide la lista en 'n' partes
def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

# Crea las 9 lista de números
def crear_lista():
    lista = []
    for i in range(9):
        lista_temporal = ""
        for j in range (1, 10):
            lista_temporal = j
            lista.append(lista_temporal)
    return lista

# Hacemos random las sublistas
def random_lista(lista):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            random.shuffle(lista[i])
    #print(str(lista))

# Rehacer la matriz (cuadrada)
def rehacer_matriz(matriz):
    temp_num = 0
    lista = []
    
    for k in range(3):
        for i in range(len(matriz)):
            temp_fila = ""
            temp_index = 0
            for j in range(0 + temp_num, len(matriz)):
                if (temp_index == 3):
                    break
                else:
                    temp_fila = str(matriz[i][j])
                    lista.append(temp_fila)
                    temp_index += 1
        temp_num += 3
    return lista  

# Reordenar listas
def reordernar_lista(lista):
    listaA = []
    listaB = []
    listaC = []
    listaD = []
    
    for i in range(len(lista)):
        if (i == 0 or i == 3 or i == 6):
            listaA.append(lista[i])
        elif (i == 1 or i == 4 or i == 7):
            listaB.append(lista[i])
        elif (i == 2 or i == 5 or i == 8):
            listaC.append(lista[i])
    
    """
    print("LISTA A")
    print(str(listaA))
    print("LISTA B")
    print(str(listaB))
    print("LISTA C")
    print(str(listaC))
    """
    
    #print("************")
    listaD = listaA + listaB + listaC
    #print(str(listaD))
    return listaD
    
# Dibuja la matriz (cuadrada)
def crear_matriz(matriz):
    for i in range(len(matriz)):
        fila = ""
        if (i == 0):
            fila += str("  -----------------------\n")
        for j in range(len(matriz)):
            if matriz[i][j] == "**":
                fila += str(matriz[i][j]) + " "
            else:
                if (j == 0):
                    fila += str(" | " + str(matriz[i][j]) + " ")
                elif (j % 3 == 2):
                    fila += str(matriz[i][j]) + " | "
                else:
                    fila += str(matriz[i][j]) + " "
        if (i % 3 == 2):
            fila += str("\n  -----------------------")
                
        print(fila)

# Asignamos una lista
lista_original = crear_lista()

# Hacemos un split a la lista para tener una lista de listas, es decir, nuestra matriz
lista = list(chunks(lista_original, 9))
#print(str(lista))


# GAME
print("¡BIENVENIDO AL SODOKU! \n" )

while True:
    esJugable = False
    
    random_lista(lista)
    temp = rehacer_matriz(lista)
    temp2 = list(chunks(temp, 9))
    #print("Rehacer lista")
    #print(str(temp2))
    #print("Reordenar")
    matriz = reordernar_lista(temp2)
    crear_matriz(matriz)
    
    
    ###########COMPARACIONES
    #for i in range(len(matriz)):
        #for j in range(len(matriz)):
            
            #if str(j) not in matriz[i][j]:
                #esJugable = True
            #else:
                #continue
    break        
    #if esJugable == True:
        #break