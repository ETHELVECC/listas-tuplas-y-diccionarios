# frutas = ['naranja', 'manzana', 'frutilla', 'banana', 'mango']

# # sub_frutas= frutas[::-1]

# # print(sub_frutas)

# for i,fruta in enumerate(frutas):
#     print(f'en la posición {i}, esta la fruta: {fruta}')



# famosos=['mirta legrand', 'marcelo tienlli', 'marley', 'franchela', 'polino']
# edades = [95, 55,45,55,49]

# for famoso, edad in zip(famosos, edades):
#     print(f'el {famoso} tiene {edad} años de edad')




# palabra=input('Ingrese una palabra: ')
# vocales=['a', 'e', 'i', 'o', 'u']

# for vocal in vocales:
#     cont=0
#     for letra in palabra:
#         if letra == vocal:
#             cont+=1
#     print(f'La vocal {vocal} aparece {str(cont)} veces')


#apend() agrega elementos pero tambien agrega listas dentro de otra lista
colores = ['azul', 'rojo', 'verde', 'amarillo']
print('lista de colores antes de agregar:', colores)
coloresmono=['blanco', 'negro']
colores.append(coloresmono)
print('lista de colores antes de agregar:', colores)


#extende() agrega una lista a otra lista como elementos
colores = ['azul', 'rojo', 'verde', 'amarillo']
print('lista de colores antes de agregar:', colores)
coloresmono=['blanco', 'negro']
colores.extend(coloresmono)
print('lista de colores antes de agregar:', colores)


#insert inseta un elemento en un determinado lugar en la lista
colores = ['azul', 'rojo', 'verde', 'amarillo']
print('lista de colores antes de agregar:', colores)
colores.insert(3,'blanco')
print('lista de colores antes de agregar:', colores)


#remove remueve un elemento
colores = ['azul', 'rojo', 'verde', 'amarillo']
print('lista de colores antes de agregar:', colores)
colores.remove('verde')
print('lista de colores antes de agregar:', colores)


#del remueve por rangos
colores = ['azul', 'rojo', 'verde', 'amarillo']
print('lista de colores antes de agregar:', colores)
del colores [0:2]
print('lista de colores antes de agregar:', colores)

#pop remueve la ultima posicion o una psocion específicas
colores = ['azul', 'rojo', 'verde', 'amarillo']
print('lista de colores antes de agregar:', colores)
colores.pop(3)
print('lista de colores antes de agregar:', colores)
