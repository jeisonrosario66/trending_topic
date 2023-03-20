import pandas as pd
import mysql.connector
import re
import emoji

# Conxion con base de datos
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="trending_topic"
)

tablaNombre = "nombreTabla"
df = pd.read_excel("Archivo.excel")

def analisiExploratorio(df, tablaNombre):
    #toda palabra que inicie con @ y tengo entre 2-15 caracteres
    twitterUser = re.compile('@[\w]{2,15}') 
    # toda palabra que empice con https-//-cualquier caracter-un .-cualquier caracter en rangos,minimo uno-/-cualquier caracter en rangos,minimo dos
    url = re.compile('https?:\/\/[\w/][\.][a-zA-Z0-9]{1,}[\/][a-zA-Z0-9]{2,}')
    #
    hashtag = re.compile('#[\w]{2,}') 
    
    # Suelto columna irrelevante para el caso
    df = df.drop(['Usuario'], axis=1)
    # Elimina filas duplicadas
    df = df.drop_duplicates()
    
    for row in df.itertuples():
        #------------------- Datos limpios Pt.1--------------------  
        # Elimina los @usuarios
        tweet = str(row[1])
        #print("\n---------------------------------------------------- Original ------------------------------------------------------")
        #print(f"{row[0]}: {tweet} len({len(tweet)})")
        for i in twitterUser.findall(row[1]):
            tweet = tweet.replace(f'{i}','').strip()
        #------------------- Datos limpio Pt.2--------------------  
        #elimina la forma https://t.co/GDMtToiiae
        for i in url.findall(row[1]):
            tweet = tweet.replace(f'{i}','').strip()
            #------------------- Datos limpio Pt.3--------------------  
        #elimina la forma #hashtag
        for i in hashtag.findall(row[1]):
            tweet = tweet.replace(f'{i}','').strip()
        #------------------- Datos limpio Pt.4--------------------  
        # Elimina los emojis
        for caracter in row[1]:
            if emoji.is_emoji(caracter) == True:
                tweet = tweet.replace(f"{caracter}","")
           
        #print("---------------------------------------------------- Procesado ------------------------------------------------------")       
        #print(f"{row[0]}: {tweet} len({len(tweet)})")
        
        sql = f"INSERT INTO {tablaNombre} (id, tweet) VALUES (%s, %s)"
        val = (row[0], tweet)
        mycursor.execute(sql, val)

mycursor = mydb.cursor()
mycursor.execute(f"CREATE TABLE IF NOT EXISTS {tablaNombre} (id INT NOT NULL, tweet VARCHAR (400) NOT NULL, PRIMARY KEY (id)) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4 COLLATE = utf8mb4_spanish_ci")
analisiExploratorio(df, tablaNombre)

# Confirma la insersion en la base de datos
mydb.commit()

print("Datos insertados")