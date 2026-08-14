import os
import pandas as pd

archivo = "mis_contraseñas.csv"

#Creamos archivo csv si no existe
def cargar_datos():

    if not os.path.exists(archivo):
        df = pd.DataFrame(columns=["Web", "Usuario", "Contraseña"])
        df.to_csv(archivo, index=False)
    return pd.read_csv(archivo)

#Añadir contraseña

def añadir_contraseña(Web, Usuario, Contraseña):
    df=cargar_datos()

    nueva=pd.DataFrame([{"Web": Web, "Usuario": Usuario, "Contraseña": Contraseña}])

    df=pd.concat([df, nueva], ignore_index=True)
    df.to_csv(archivo, index=False)
    print(f'\n!Datos de {Web} guardados!')

#Para buscar
def buscar(Web):
    df=cargar_datos()
    resultado=df[df["Web"].str.lower()==Web.lower()]

    if not resultado.empty:
        print("\n--- Credenciales encontradas ---")
        print(resultado.to_string(index=False))
    else:
        print(f"\nNo se encontraron credenciales para: {sitio}")

#Para eliminar

def eliminar(Web):
    df=cargar_datos()

    if not df[df["Web"].str.lower()==Web.lower()].empty:
        df = df[df['Web'].str.lower() != Web.lower()]
        df.to_csv(archivo, index=False)
        print(f"\n¡Se han eliminado las credenciales de: {Web}!")
    else:
        print(f"\nNo se encontró ningún registro para: {Web}")

#
eliminar("Netflix")
     