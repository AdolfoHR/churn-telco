import sqlite3
import pandas as pd

#Rutas
RUTA_CSV = "data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv"
RUTA_DB = "data/churn.db"

#1.Lectura de los archivos cvs
df = pd.read_csv(RUTA_CSV)
print(f"CSV leído: {df.shape[0]} filas, {df.shape[1]} columnas")

#2.Se realiza la conexión a la base de datos
conexion = sqlite3.connect( RUTA_DB)

#3.Los datos los guardamos en una tabla llamada "clientes"
df.to_sql("clientes", conexion, if_exists="replace", index=False)

# 4. Verificar que quedaron guardados
total = pd.read_sql("SELECT COUNT(*) AS total FROM clientes", conexion)
print(f"Filas en la tabla 'clientes': {total['total'][0]}")

conexion.close()
print("Base de datos creada en", RUTA_DB)