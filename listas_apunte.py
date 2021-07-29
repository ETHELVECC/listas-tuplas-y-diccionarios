#CONOCER LA CANTIDAD DE ELEMENTOS DE LA LISTA>>>>> LEN
# lista=["hola", "chau"]
# cantidad_de_elementos=len(lista)
# print(cantidad_de_elementos)

# print(len(lista)) #HACIENDO ESTE PASO NOS AHORRAMOS LA LINEA 3 Y 4


##ACCEDER POR A LOS ELEMENTOS POR SUS ÍNDICES
###LOS ÍNDICES COMIENZAN EN 0
# estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
# print(estaciones[0]) #IMPRIME EN CONSOLA EL ELEMENTO QUE SE ENCUENTRE EN LA POSICIÓN 0
# print(estaciones[1]) #IMPRIME EN CONSOLA EL ELEMENTO QUE SE ENCUENTRE EN LA POSICIÓN 1
# print(estaciones[2]) #IMPRIME EN CONSOLA EL ELEMENTO QUE SE ENCUENTRE EN LA POSICIÓN 2
# print(estaciones[3]) #IMPRIME EN CONSOLA EL ELEMENTO QUE SE ENCUENTRE EN LA POSICIÓN 3
# print(estaciones[-1]) #IMPRIME EN CONSOLA EL ELEMENTO QUE SE ENCUENTRE EN LA POSICIÓN 3
# print(estaciones[-3]) #IMPRIME EN CONSOLA EL ELEMENTO QUE SE ENCUENTRE EN LA POSICIÓN 1


# ###MODIFICAR ELEMENTOS
# mascotas =['gato', 'perro', 'loro', 'hámster', 'iguana', 'poni']
# mascotas[4] = 'acuario'   #se modifica el elemento del índice 4
# print(mascotas)           #al realizar la impresión en consola figura la nueva lista


##RECORRER LISTA
### UTILIZANDO UN CICLO FOR
# lista=['a','b','c','d']             ###creada la lista
# # for index in range(0, len(lista)):   #para indice en el rango de 0, len(lista) equivale al recorrido de la lista
# #     print(lista[index])             #imprime en consola, la lista segun los índice recorridos


# for i in lista:      #una forma más sencilla es nombrar i a los elementos
#     print(i)         #solicitar impresión de i


##AGREGAR ELEMENTOS A UNA LISTA con append() aquí se agrega el elemento al final de la lista
# farmacia=['curitas', 'algodón', 'aspirina'] #creada la lista
# print(farmacia)                             #realizar la impresión
# farmacia.append('shampoo')                  #método append para agregar shampoo
# print(farmacia)                             #realizar una nueva impresión para comprobar que se ha agregado el elemento
# farmacia.append('acondicionar')             #método append para agregar ACONDICIONADOR
# print(farmacia)                             #realizar una impresión para comprobar que se ha agregado


# ####AGREGAR ELEMENTOS A UNA LISTA con insert( , ) aquí podemos ubicar el elemento donde queremos ubicar
# farmacia.insert(2, 'pañal')     #se indica el índice del lugar y luego el elemento
# print(farmacia)                 #con la impresión comprobamos


# ### AGREGAR TODOS LOS ELEMENTOS DE UNA LISTA A OTRA LISTAS CON EXTEND()
# #ya tenemos creada la lista farmacia, y crearemos una nueva para agregarle los elementos
# compras_semanales=['talco', 'desodorante', 'loción', 'crema humectante'] #creada la lista hacemos impresión
# print(compras_semanales)
# compras_semanales.extend(farmacia)    #a compras semanales se le agrega farmacia, por eso va dentro de extend()
# print(compras_semanales)


##REBANADAS - SUBLISTAS O SLICING    [m:n]
# variables=['x', 'y', 'z', 'w', 'a', 'b', 'c', 'm', 'q']
# mini_cudric=variables[4:7]     #si quisiera tomar los valores a, b y c debo indicar el 1er indice 4 
# #y uno posterior al que quiero(6),entonces coloco 7
# print(mini_cudric)

# mini_lineal=variables[7:] #si quiero tomar desde cierto indice al final, dejo vacio n
# print(mini_lineal)

# mini_sistema=variables[:4] #si quiero tomar desde el principio y hasta el índice 3, dejo vacio m y coloco 4
# print(mini_sistema)


# ###MÉTODO COPY()
# #Tomando el ejemplo anterior de la lista variables la copiare bajo el nombre incógnitas
# incognitas=variables.copy()
# print(incognitas)


###MÉTODO SORT PARA ORDENAR UNA LISTA
# numeros=[24, 9, 82, 7, 10, 8, 12, 6, 14]
# print(numeros)
# numeros.sort()          #ordena los elementos en forma decreciente
# print(numeros)

# numeros.sort(reverse=True) #pasando el parámetro reverse=True los ordena de manera decreciente
# print(numeros)

# numeros[::-1] #otra forma de invertir es haciendo un doble slicing o recorrido
# print(numeros)

# numeros.reverse()   #ordena la lista en forma inversa a la dada.
# print(numeros)


###SABER SI UN ELEMENTO
# num=[24, 9, 82, 7, 10, 8, 12, 6, 14, 17, 12, 56, 25, 6, 50]
# #SI UN ELEMENTO ESTÁ EN LA LISTA OPERADOR IN
# print(7 in num)   #si el elemento está arroja el booleano True
# print(1 in num)   # si no está arroja el valor False por consola

# #CUANTAS VECES SE ENCUENTRA EL ELEMENTO DENTRO DE LA LISTA METODO COUNT()
# num.count(12)
# print(num.count(12))      #debo hacer print para ver el resultado por consola

# #CONOCER EL ÍNDICE MÉTODO INDEX()
# indice=num.index(82)      #para conocer el lugar que ocupa 82 en la lista
# print(indice)             #imprime 2, que es el indice
# print(num[indice])        #imprime en número que fue que ocupa el indice anterior

# print(num.index(6))  #en caso de haber un elemento repetido, index() solo devuelve la 1er posición


###ELIMINAR ELEMENTOS
# #UTILIZANDO LA PALABRA RESERVADA del 
# num=[24, 9, 82, 7, 10, 8, 12, 6, 14, 17, 12, 56, 25, 6, 50]
# print(num)
# del num[7]   #elimina el elemento de índice 7
# print(num)
 
# del num[:3]     #elimina una sublista o rebanada
# print(num)

# #UTILIZANDO REMOVE()
# num.remove(56)      #elimina directamente el elemento 56
# print(num)

# #UTILIZANDO POP()
# quitar = num.pop()   #sin parametro, quita el último elemento de la lista
# print(quitar) #aquí nos indica que elemento quitó
# print(num)    #aquí nos devuelve la nueva lista sin el elemento

# quitar = num.pop(10)   #con parametro, quita el elemento que indica el índide pasado
# print(quitar) #aquí nos indica que elemento quitó
# print(num)     #aquí nos devuelve la nueva lista sin el elemento


###FUNCIONES
variables=['x', 'y', 'z', 'w', 'a', 'b', 'c', 'm', 'q']
mini_cudric=variables[4:7]    
print(mini_cudric)

mini_lineal=variables[7:] 
print(mini_lineal)

mini_sistema=variables[:4] 
print(mini_sistema)

#LEN PARA CONOCER LA LONGITUD O CANTIDAD DE ELEMENTOS
longitud=len(variables)
print(longitud)     #resultado por consola es 9 elementos

#MIN PARA SABER EL ELEMENTO MENOR DE LA LISTA
minimo=min(variables)
print(minimo)

#MAX PARA SABER EL ELEMENTO MAYOR DE LA LISTA
maximo=max(variables)
print(maximo)

#SUM para sumar los elementos que componen una lista
num=[24, 9, 82, 7, 10, 8, 12, 6, 14, 17, 12, 56, 25, 6, 50]
suma=sum(num)
print(suma)  #arroja por consola 338, el resultado de sumar todos los valores de los elementos

###operadores matemáticos
otra = mini_cudric + mini_lineal    #Aquí se suman dos listas
print(otra)


mini_cudric+=['Vértice', 'Raices']   #agrega dos elementos al final de la existente
print(mini_cudric)


multilineal=mini_lineal*2
print(multilineal)       #la nueva lista repite los elementos la cantidad de veces que indique *n
