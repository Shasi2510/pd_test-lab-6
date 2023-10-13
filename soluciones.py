import pandas as pd
import requests

def ej_1_cargar_datos_demograficos() -> pd.DataFrame:
    df = pd.read.csv("us-cities-demographics.csv")
    datos_demograficos = df["AlphabeticCode"].tolist()
    return datos_demograficos

def ej_2_cargar_calidad_aire(ciudades: Set[str]) -> None:
    resultado = []
    for datos_demograficos in ciudades:
        api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(city)
        response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
        if response.status_code == requests.codes.ok:
            calidad_del_aire = response.json()['air quality']
            resultado.append((ciudad, calidad_del_aire))
    resultado = pd.DataFrame(resultado, columns=['ciudad', 'calidad_del_aire'])
    resultado = resultado.sset_index("datos_demograficos")
    resultado.to_csv('ciudades.csv')    
    return resultado

resultado.drop(["Race", "Count", "Number of Veterans"], axis=1, inplace=True)
resultado.drop_duplicates(inplace=True)
