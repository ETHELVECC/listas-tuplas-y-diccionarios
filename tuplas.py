# ### las tupals se definen por parentesis
# ### pueden definise empaquetada o desdempaquetada

#CREAR TUPLAS
# tupla =()   ### tupla vacia
dni = (12807388, 8301230, 29724675) 


###PARA DESEMPAQUETAR UN TUPLA EMPAQUETADA
# impares=1,3,5,7
# x, y, w, z, = impares  ###para desempaquetar
# print (x)
# print (y)
# print (w)
# print (z)
# print(impares)


# #ACCEDER A SUS ELEMENTOS POR SUS ÍNDICES
# dias ='lunes', 'martes', 'miercoles', 'jueves', 'viernes'   ### empaquetada
# print(dias[3])   #Impresión de la lista y los índices van entre [] devuelve elemento Jueves
# print(dias[-1])     #Con índices negativos comienza a imprimierlos de atrás devuelve elemento viernes

# #se puede obtener con slicing [:]
# print(dias[1:3])    #La devulución es una subtupla desempaquetada
# print(dias[:2])        #devuelve una subtupla desdempaquetada 
# print(dias[::-1])    #devuelve una subtupla desempaquetada en forma inversa a la dada

# #FUNCIONES LEN, MAX MIN Y SUM
# cuadra_dos=(0, 2, 4, 8, 16, 32, 64, 128)

# longitud=len(cuadra_dos)   #puedo definir una nueva variable que me devuelve la cantidad de elementos e imprimir
# print(longitud)
# print(len(cuadra_dos))  #puedo directamente imprimir el len(lista) y obtengo la cantidad de elementos

# maximo=max(cuadra_dos)   #puedo definir una nueva variable que me devuelve el maximo valor de los elementos e imprimir
# print(maximo)
# print(max(cuadra_dos))  #puedo directamente imprimir el max(lista) y obtengo el valor máximo de los elementos

# minimo=min(cuadra_dos)   #puedo definir una nueva variable que me devuelve el mínimo valor de los elementos e imprimir
# print(minimo)
# print(min(cuadra_dos))  #puedo directamente imprimir el min(lista) y obtengo el valor mínimo de los elementos

# suma=max(cuadra_dos)   #puedo definir una nueva variable que me devuelve la suma de todos los elementos e imprimir
# print(suma)
# print(sum(cuadra_dos))  #puedo directamente imprimir el sum(lista) y obtengo la suma de todos los valores de los elementos


# #METODOS COUNT() E INDEX()
# granja=('caballo', 'vaca', 'gallina', 'pavo', 'caballo', 'chivo', 'oveja', 'chivo', 'pollo','chivo')

# print(granja.count('chivo')) # el método lista.count(elemento) me indica las veces que se repite ese elemento
# #en este caso el resultado por consola es 3 xq 3 veces aparece en la lista el elemento chivo
# print(granja.count('yegua')) # en este caso el resultado por consola es 0 xq no existe el elemento yegua


# print(granja.index('pollo'))  #el método lista.index(elemento) me indica en que índice-ubicación está
# print(granja.index('cerdo')) #para el caso que el elemento no esté en la lista, informa q no está en la lista


#TUPLAS COMO RESULTADO DE FUNCIONES
# def multivalor():           #definir la función
#     return 'a', 'b', 5, 7, 'false'

# resultado=multivalor()     # asignar un valor a la función
# print(resultado)

# x, y, z, w, q = multivalor() #otra forma es desempaquetar los resultado de la función multivalor
# print(multivalor())


# #CREAR TUPLA A PARTIR DE UNA LISTA Y VICEVERSA
# tupla=(1,4,6,10)   #dada la tupla aplicar el método list(nombre de la tupla) e imprimir
# lista=list(tupla)  
# print(lista)        #resultado por consola es una lista [1,4,6,10]

# lista_1=['a','b','c','d']  #dada la lista aplicar el método tuple(nombre de la lista) e imprimir
# tupla_1=tuple(lista_1)
# print(tupla_1)      #resultado por consola es una tupla ('a','b','c','d')

##CREAR LISTA O TUPLAS A PARTIR DE UNA CADENA DE CARACTERES METODO LIST()
# lista=list('soy ethel')    #aplicando el método list(cadena) y luego imprimir
# print(lista)                #El resultado es un lista, que incluye los espacios vacíos

# tupla=tuple('I am ethel')  #de manera análoga se puede hacer con una tupla
# print(tupla)


##LIST COMPREHESION  PARA CREAR LISTAS CON ELEMENTOS ITERABLES
#ejemplo crear una lista con los primeros digitos
digitos=[]         # así se procedería con un ciclo for
for i in range(0, 10):
    digitos.append(i)
print(digitos)

digital=[i for i in range(0,10)]    #de manera eficiente
print(digital)

reiterado=['luna' for i in range(0,5)]   #repite el mismo elemento la cantidades de veces del rango
print(reiterado)

##otro uso de list comprehension
#dada una lista, queremos que la lista contega los primeros elementos com mayuscula
capitales=['resistencia', 'corrientes', 'posadas', 'rosario']

capitales_mayus=[]     #con un ciclo for
for n in capitales:
    capitales_mayus.append(n.capitalize())
print(capitales_mayus)

capi_mayus=[i.capitalize()for i in capitales]    #de manera eficiente
print(capi_mayus)


#LIST COMPREHENSION PARA CREAR MATEMÁTICOS
#QUEREMOS CREAR EL DUPLICADO Y EL TRIPLICADO DE UNA LISTA DADA
simple=[7, 12, 43]

doble=[x*2 for x in simple]
print (doble)

triple=[y*3 for y in simple]
print(triple)



#AGREGAR UNA TUPLA A OTRA TUPLA
# impares=1,3,5,7
# tupla=(1,5,'A',5,[0,1,2,3], True, impares)

# print(tupla)

#SABER QUE CLASE ES 
# dias ='lunes', 'martes', 'miercoles', 'jueves', 'viernes'   ### empaquetada
# print(dias, type(dias)) 
