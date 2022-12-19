nombre_1 = (input('Nombre de usuario1: '))
edad_1 = int(input('Edad de usuario1: '))
nombre_2 = (input('Nombre de usuario2: '))
edad_2 = int(input('Edad de usuario2: '))

if edad_1 > edad_2:
    print(f'{nombre_1} tiene mayor edad que {nombre_2}')
elif edad_1 < edad_2:
    print(f'{nombre_2} tiene mayor edad que {nombre_1}')
else:
    print('Ambos tienen edades iguales')