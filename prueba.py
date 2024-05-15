'''Este algoritmo maneja el stock de productos de la bodega de AQUI VENDEMOS

'''
import os

stock = {'1' : ['Escoba', 5],
         '2' : ['Huevos', 25],
         '3' : ['Leche', 9]}

menup = ['Ver stock de productos', 'Añadir nuevo producto', 'Ajustar stock', 'Eliminar producto', 'Salir']
print('******************************\n****Administrador de Stock****\n******************************\n')
while True:
    for i, opt in enumerate(menup, start=1):
        print(f'{i}. {opt}')
    ans = input('¿Que quieres hacer?\n')
    if ans == '1':
        os.system('cls')
        for llave, valor in stock.items():
            print(f'{llave}\nProducto: {valor[0]}\nStock: {valor[1]}\n')
    elif ans == '2':
        os.system('cls')
        producto = input('Ingrese el nombre del nuevo producto:\n')
        if not producto.replace(' ','').isalpha():
            os.system('cls')
            print('Error: el producto solo puede contener caracteres alfabeticos.\n')
            continue
    elif ans == '3':
        os.system('cls')
        producto = input('Ingrese el nombre del producto a ajustar:\n')
        if not producto.replace(' ','').isalpha():
            os.system('cls')
            print('Error: el producto solo puede contener caracteres alfabeticos.\n')
            continue
        cantidad = input('Ingrese el nuevo stock del producto:\n')
        if not cantidad.isnumeric():
            os.system('cls')
            print('Error: la cantidad del producto solo puede contener numeros.\n')
    elif ans == '4':
        os.system('cls')
        for llave, valor in stock.items():
            print(f'{llave}\nProducto: {valor[0]}\nStock: {valor[1]}\n')
            ans = input('¿Que producto desea eliminar?\n')
    elif ans == '5':
        os.system('cls')
        exit('Adios!\n')
    else:
        os.system('cls')
        print('Error: ingresa una opcion valida\n')
