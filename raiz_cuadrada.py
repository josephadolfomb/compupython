objetivo = int(input('Escoge un número: '))
busqueda = input('Escoge un tipo de búsqueda binaria o aproximacion: ')

def bbinaria (objetivo):
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def aproximacion (objetivo):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon: 
        print (f'No se encontró la raíz cuadrada del {objetivo}')
    else: 
        print(f'la raiz cuadrada de {objetivo} es {respuesta}')

if busqueda == 'binaria':
    bbinaria(objetivo)
elif busqueda == 'aproximacion':
    aproximacion(objetivo)
else: 
    print('Eliga una busqueda binaria o aproximacion, intente otra vez')