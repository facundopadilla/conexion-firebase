# Acá se realizan las conexiones y autenticaciones

from firebase import firebase

# Conexión a la base de datos (si se conecta correctamente no devuelve ninguna información)
def conexion():
    try:
        conexion = firebase.FirebaseApplication('https://mitienda-1cc7e.firebaseio.com/', None)
        return conexion
    except:
        print(">>> Error: no se pudo conectar...")

# Obtengo la base de datos, luego selecciono una tabla y muestro los elementos
def operar(conexion):
    print("\n--- Bases de datos de FireBase ---")
    base = obtenerBD(conexion.get("",None))
    print("\n--- Seleccione una tabla ---")
    tabla = obtenerTablas(conexion.get(base,None))
    mostrarTablas(conexion.get(base+"/"+tabla,None))

def obtenerBD(conexion):
    try:
        base = [i for i in conexion]
        for i,j in enumerate(base):
            print(f"[{i}] {j}")
        opcion = int(input("\n >>>Selecciona la base de datos: "))
        return base[opcion]
    except:
        print("\n>>> Error: no existen bases de datos...")

# Recibe como parámetro la base de datos, en caso de que hayan tablas las muestra, sino hay nada, muestra error
def obtenerTablas(base):
    try:
        tabla = [i for i in base]
        for i,j in enumerate(tabla):
            print(f"[{i}] {j}")
        opcion = int(input("\n>>> Selecciona una tabla: "))
        return tabla[opcion]
    except:
        print("\n>>> Error: No existen tablas...")

# Recibe como parámetro la tabla, si no hay elementos devuelve un error
def mostrarTablas(tabla):
    try:
        for i,j in enumerate(tabla):
            print(f"[{i}] {j}")
    except:
        print("\n>>> Error: no hay elementos que mostrar...")