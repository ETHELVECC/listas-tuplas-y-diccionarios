# ### ejemplos de diccionarios

# coordenadas = {'x':34, 'y':23, 'z':45}

# agenda_telefonica ={
#     'sandra':456773,
#     'pedro':378475,
#     'lorena':483758,
#     'juan':578493
# }

# seleccion_futbol = {
#     1:'sergio almiron',
#     2:'sergio batista',
#     3:'ricardo bochini',
#     4:'claudio borghi',
#     5:'luis brown',
#     6:'daniel pasarella',
#     7:'jorge burruchaga',
#     8:'nestor clausen',
#     9:'luis cuciuffo',
#     10:'diego maradona',
#     11:'jorge valdano'
# }

# alumno = {'nombre':'marcos', 'materia':['matemática', 'biología', 'diseño']}

# ###para acceder a los elementos del diccionario se utiliza la calve del diccionario

# print (coordenadas['x'])
# print(agenda_telefonica['sandra'])
# print(seleccion_futbol[10])
# print(alumno['nombre'])
# print(alumno['materia'])
# # print(alumno['edad']) # nos arroja un error por consola xq no existe la llave

# ### diccionarios vacío
# diccionario = {}

# diccionario = dict()


# ##modificar valor
# usuario={'nombre':'juan', 'edad':23}
# print(usuario)         ###se da la orden de imprimir el diccionario
# usuario['edad']=24
# print (usuario)          ### devuelve el diccionario corregido

# #### para agregar llaves se procede de forma similar
# usuario['apellido']='perez'         ###se agrega una llave al diccionario
# print(usuario)

# ###setdefaul otra forma de agregar elementos, solo en el caso
# ###de que la llave no exista
# usuario.setdefault('comida_favorita','ninguna')
# print(usuario)

# ###METODO GET
# color=usuario.get('color_favorito')     ###como no existe la llave arroja valor none
# print(color)
# apellido=usuario.get('apellido')        ###como existe apellido arroja el perez el valor guardado en la llave
# print(apellido)

##RECORRER UN DICCIONARIO
#ciclo for
dicc={'a':11, 'b':22, 'c':33, 'd':44, 'e':55}
print(dicc)
# for key in dicc:
#     print('la clave es: ', key)
#     print('su valor es: ', dicc[key])
#     print('la clave es:', key, 'y su valor es:', dicc[key])

# #MÉTODO ITEMS()
# print(dicc.items())

# for key, value in dicc.items():
#     print(key, ':', value)


# #VERIFICAR SI SE ENCUENTRA UNA CLAVE EN UN DICCIONARIO
# #usando operador in y solicitando la impresión 
# print('a' in dicc) #arroja por consola el valor True xq existe
# print('g' in dicc) #arroja false xq no existe

# #usando condicional if le decimos que si está b que imprima el valor
# if 'b' in dicc:     
#     print(dicc['b'])

##ELIMINAR ELEMENTOS
##UTILIZANDO LA PALABRA RESERVADA DEL
# del dicc['e']
# print(dicc) #me devuelve el diccionario sin elemento guadado bajo la key e


##uTILIZANDO POP() siempre se debe pasar la key como parámetro del pop
# diccion={'fondo_color':'negro', 'texto_color':'blanco', 'size_fuente':12}
# print(diccion)   #imprime el diccionario anterior
# quitar =diccion.pop('fondo_color')     #crear una variable quitar y solicitar impresion
# print(quitar)


# print(diccion.pop('fondo_color')) #impresión del método pop y solicitar la impresión de nuevo 
# print(diccion)

# ##MÉTODO CLEAR() BORRA TODA LOS ELEMENTOS DE UN DICCIONARIO
# print(diccion.clear()) #pasando dentro del print el metodo clear()
# print(diccion)


##EXTENDEER DICCIONARIOS METODO UPDATE()
##SI LAS CLAVES YA EXISTEN, SE ACTUALIZAN LOS VALORES DE LAS KEYS
##SI LAS CLAVES NO EXISTEN, SE CREAN NUEVOS 'KEY':'VALUE'
