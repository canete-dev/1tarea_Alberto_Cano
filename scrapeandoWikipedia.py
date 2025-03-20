import requests
from bs4 import BeautifulSoup

url = 'https://es.wikipedia.org/wiki/Espa%C3%B1a'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # print(soup.prettify()) esto es para ponerlo bonito

    # Buscar la tabla infobox que contiene la información
    table = soup.find('table', {'class': 'infobox'})

    # Inicializar un diccionario para almacenar los datos
    datos = {}

    # Iterar sobre las filas de la tabla    
    for i in table.find_all('tr'):
        # Buscar la celda de encabezado y la celda de datos
        header = i.find('th')
        data = i.find('td')

        # Comprobar que existen y obtener los datos en una variable
        # el find_next es porque en la wikipedia es el siguiente td el que corresponde al th que buscamos
        if header and data:
            header_text = header.get_text(strip=True).lower()
            data2 = data.find_next('td')
            data_text = data2.get_text(strip=True)

            # Extraer y asignar los valores correspondientes
            if 'población' in header_text:
                datos['población'] = data_text
            elif 'pib' in header_text:
                datos['PIB'] = data_text
            elif 'superficie' in header_text:
                datos['superficie'] = data_text
                

    # Mostrar los datos extraídos con la primera en mayuscula, esta es la manera de recorrer un diccionario imprimiendo keys y values
    for key, value in datos.items():
        print(f"{key.capitalize()}: {value}")
        