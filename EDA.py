import pandas as pd
import mysql.connector

# Conxion con base de datos
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="trending_topic"
)
# Datos a insertar
df = pd.read_excel("ARCHIVO")

# Suelto columna irrelevante para el caso
df = df.drop(['Usuario'], axis=1)

# Conteo de filas antes de eliminar duplicados
# print(df.count())

# Elimina filas duplicadas
df = df.drop_duplicates()
# print(df.count())

# Detecta filas vacias (Si existen)
# print(df.isnull().sum()) 

tablaNombre = "tabla_nombre"
cantidadCaracteres = 0

# Cuenta la cantidad de caracteres en cada fila
for row in df.itertuples():
    if len(row[1]) > cantidadCaracteres:
        cantidadCaracteres = len(row[1])
else:
    pass

mycursor = mydb.cursor()
mycursor.execute(f"CREATE TABLE IF NOT EXISTS {tablaNombre} (id INT NOT NULL, tweet VARCHAR ({cantidadCaracteres}) NOT NULL, PRIMARY KEY (id)) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4 COLLATE = utf8mb4_spanish_ci")
 
# Sentencias a ejecutar
for row in df.itertuples():
    sql = f"INSERT INTO {tablaNombre} (id, tweet) VALUES (%s, %s)"
    val = (row[0]+1, row[1])
    mycursor.execute(sql, val)

# Confirma la insersion en la base de datos
mydb.commit()

print("Datos insertados")
