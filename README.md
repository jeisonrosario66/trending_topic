Esto es un proyecto de Jeison Rosario para Digital Nao

De ninguna manera es una bifurcación de  “snscraper”

Bibliotecas requeridas
  - pandas
  - snscrape
  - mysql
  
El flujo de ejecucion es sencillo
- scraper.py
    - Este genera los datos para seguir con el flujo
- EDA.py
    - Recibe los datos generados para almacenarlos
    - Este codigo da por echo que ya tiene una base de datos configurada
    
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="trending_topic"
        )
        
![Captura](https://user-images.githubusercontent.com/96961824/225119524-0f0fe6ba-ac36-44a7-a92b-2784bc215b22.PNG)
