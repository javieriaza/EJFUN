import shutil
import requests
import time
import urllib.request
import os

lisa= 'Lisa Simpson'
homer= 'Homer Simpson'
diccionario={}
w=0

while True: #Generamos bucle con tiempo 3 segundos que nos introduzca en el diccionario el contador de palabras
 time.sleep(3)
 respuesta=requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')
 respuesta.json()
 frase=respuesta.json()[0]['quote'] 
 personaje=respuesta.json()[0]['character']
 imagen=respuesta.json()[0]['image'] 
 texto={'frase': frase,'personaje': personaje} 
 file=(f"Esta es la foto de {personaje}.png")
 if not(os.path.exists(personaje)):
        #Descarga de la imagen
        r=urllib.request.urlopen(imagen)
        f=open(file,'wb')#Abrir
        f.write(r.read())#Comprobar 
        f.close()#Cerrar
        os.mkdir(personaje)
        shutil.move(file,personaje)#A la izquierda que quiero mover , derecha donde lo quiero mover
        
 quitar= ",.?!:;\n" #Queremos quitar caracteres de puntuación para que no cuenten como palabras
 for caracter in quitar:# Para ello generamos un bucle que quite estos signos y los remplace por un espacio
    frase=frase.replace(caracter,"")
 frase2=frase.split()
 frase=frase2 
 for a in frase:
    if a in diccionario:
        diccionario[a]=w
    else:
        diccionario[a]=w
    w=w+1 #sumando cada iteración
    print(diccionario)

       

   
  
 