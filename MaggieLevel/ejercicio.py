import requests
import time
import pandas as pd

lisa = 'Lisa Simpson'
homer = 'Homer Simpson'

while True:
 respuesta=requests.get('https://thesimpsonsquoteapi.glitch.me/quotes') #Llamada a la Api de la que importamos frases , personajes e imágenes
 respuesta.json()
 frase=respuesta.json()[0]['quote'] #Recogemos la frase en una variable
 personaje=respuesta.json()[0]['character']#Recogemos el personaje en una variable
 imagen=respuesta.json()[0]['image']#Recogemos la imagen
 texto={'frase': frase, 'personaje': personaje}# Generamos una variable diccionario que recoje la frase y el personaje que la dice
 output=pd.DataFrame() #Con el uso de pandas y condicionales realizaremos la introducción de cada frase en su respectiva carpeta
 if personaje == lisa :
    output=pd.DataFrame()
    output=output.append(texto,ignore_index=True)
    print(output.head())
    output.to_csv("MaggieLevel/Lisa/lisa.csv" , mode='a')
 elif personaje == homer:
    output=pd.DataFrame()
    output=output.append(texto,ignore_index=True)
    print(output.head())
    output.to_csv("MaggieLevel/Homer/homer.csv" , mode='a')
 else:
    output=pd.DataFrame()
    output=output.append(texto,ignore_index=True)
    print(output.head())
    output.to_csv("MaggieLevel/General/general.csv" , mode='a')

 time.sleep(30)



