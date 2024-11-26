def decorador_mensaje(func):
    def wrapper():
        print("Comenzando la ejecucion.")
        func()
        print("Terminando la ejecucion.")
    return wrapper


@decorador_mensaje
def otra_funcion():
    print("Ejecutando otra función.")


# Probando
otra_funcion()
# Salida
# Comenzando la ejecucion.
# Ejecutando otra funcion.
# Terminando la ejecucion.
