while True:
    print("""
        Seleccione el proceso que desea aplicar
        1: Ingresar puntuación y comentario
        2: Comprueba los resultados obtenidos hasta ahora.'
        3: Finalizar
        """)
    num=input("Ingrese el numero:")
    if int(num)==1:
        while True:
            point=input('Por favor, introduzca una puntuación en una escala de 1 a 5: ')
            if int(point) <= 0 or int(point) > 5:
                print('Indíquelo en una escala de 1 a 5')
            elif int(point)>0 and int(point)<=5:
                print('Por favor, introduzca un comentario')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                file_pc = open("data.txt", 'a')
                file_pc.write(f'{post} \n')
                file_pc.close()
                break
            else:
                print('Por favor, introduzca la puntuación en números')

    elif int(num) == 2:
        print('Resultados hasta la fecha.')
        read_file = open("data.txt", "r")
        print(read_file.read())
        read_file.close()
    elif int(num) == 3:
        print('Finalizando')
        break
    else:
        print('Introduzca un número del 1 al 3')