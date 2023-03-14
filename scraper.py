import snscrape.modules.twitter as sntwitter
import pandas as pd

# lista para datos de tweets
attributes_container = []

cantidadTweets = 10
palabraABuscar = "mujeres"
# Since: fecha de partida
# Until: fecha tope
# Si no espesifica fechas, tomara los tweets mas recientes
# Fecha formato: Año/Mes/Dia

# raspa datos solicitados
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{palabraABuscar} since:2023-03-07 until:2023-03-10').get_items()):
    if i>cantidadTweets:
        break
    attributes_container.append([tweet.user.username, tweet.rawContent])
    
# crea un dataframe
tweets_df = pd.DataFrame(attributes_container, columns=["Usuario", "Tweet"])

# Guarda los datos en un archivo excel
tweets_df.to_excel(f'tweets_{palabraABuscar}.xlsx', index=False)

print(tweets_df)
