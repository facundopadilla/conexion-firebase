from comandos import *

if __name__ == "__main__":
    while(True):
        print("""\n --- Menú de Firebase ---
    [1] Conectar con FireBase 
    [2] Obtener bases de datos
    [3] Salir""")
        opcion = input("\n>>> Ingresar opción: ")
        if opcion == '1':
            conectar = conexion()
        elif opcion == '2':
            if conectar != "":
                operar(conectar)
            else:
                print("\n>>> Error: conéctese a una base de datos")
        elif opcion == '3':
            print("\n>>> Finalizando programa...")
            break
        else:
            print("\n>>> Error: Ingrese una opción correcta...")
        
