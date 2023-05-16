# Importamos las dependencias necesarias:

from fastapi import FastAPI
import pandas as pd

# Creamos una instancia de la aplicación FastAPI:

app = FastAPI()

#Cargamos los datos del csv:

def cargar_datos():
    # Cargamos el archivo CSV en un DataFrame de Pandas
    df = pd.read_csv("movies_dataset_limpio.csv")
    
    return df


# Definimos las rutas y operaciones de la API mediante decoradores:

@app.get("/peliculas_mes/{mes}")
def peliculas_mes(mes):
    #Lógica para obtener la cantidad de películas estrenadas en el mes históricamente
    respuesta = obtener_cantidad_peliculas_mes(mes)
    return {'mes': mes, 'cantidad': respuesta}

@app.get("/peliculas_dia/{dia}")
def peliculas_dia(dia):
    #Lógica para obtener la cantidad de películas estrenadas en el día de la semana 
    # históricamente
    respuesta = obtener_cantidad_peliculas_dia(dia)
    return {'dia': dia, 'cantidad': respuesta}

@app.get("/franquicia/{franquicia}")
def franquicia(franquicia):
    #Lógica para obtener la cantidad de películas, ganancia total y promedio de una 
    # franquicia
    respuesta_cantidad = obtener_cantidad_peliculas_franquicia(franquicia)
    respuesta_ganancia_total = obtener_ganancia_total_franquicia(franquicia)
    respuesta_ganancia_promedio = obtener_ganancia_promedio_franquicia(franquicia)
    return {'franquicia': franquicia, 'cantidad': respuesta_cantidad,
            'ganancia_total': respuesta_ganancia_total, 'ganancia_promedio':
            respuesta_ganancia_promedio}

@app.get("/peliculas_pais/{pais}")
def peliculas_pais(pais):
    #Lógica para obtener la cantidad de películas producidas en un país
    respuesta = obtener_cantidad_peliculas_pais(pais)
    return {'pais': pais, 'cantidad': respuesta}

@app.get("/productoras/{productora}")
def productoras(productora):
    #Lógica para obtener la ganancia total y la cantidad de películas producidas
    #por una productora
    respuesta_ganancia_total = obtener_ganancia_total_productora(productora)
    respuesta_cantidad = obtener_cantidad_peliculas_productora(productora)
    return {'productora': productora, 'ganancia_total': respuesta_ganancia_total,
            'cantidad': respuesta_cantidad}

@app.get("/retorno/{pelicula}")
def retorno(pelicula):
    #Lógica para obtener la inversión, ganancia, retorno y año de lanzamiento
    #de una película
    respuesta_inversion = obtener_inversion_pelicula(pelicula)
    respuesta_ganancia = obtener_ganancia_pelicula(pelicula)
    respuesta_retorno = obtener_retorno_pelicula(pelicula)
    respuesta_anio = obtener_anio_lanzamiento_pelicula(pelicula)
    return {'pelicula': pelicula, 'inversion': respuesta_inversion, 'ganancia':
            respuesta_ganancia, 'retorno': respuesta_retorno, 'anio': respuesta_anio}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

