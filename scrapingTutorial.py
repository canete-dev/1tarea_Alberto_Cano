from bs4 import BeautifulSoup
import bs4
import requests

# Versiones
import bs4 # Solo para el chequeo
print("Versión de BeautifulSoup:",bs4.__version__)
print("Versión de requests:", requests.__version__)

# Empezamos el scraping

# 1. Obtener el HTML
URL_BASE = 'https://scrapepark.org/courses/spanish/'
pedido_obtenido = requests.get(URL_BASE)
html_obtenido = pedido_obtenido.text

# 2. "Parsear" ese HTML
soup = BeautifulSoup(html_obtenido, "html.parser")
print(type(soup)) # asi vemos el tipo

# 3. Buscar lo que queremos

# FIND
primer_h2 = soup.find('h2') # filtramos por h2
print(primer_h2) # con find se va a mostrar solo el primero
print(primer_h2.text) # Solo el texto contenido, es equivalente a: print(soup.h2.text)

# FIND_ALL
h2_todos = soup.find_all('h2')
print(h2_todos)   

# ARGUMENTOS
# Si usamos el parametro limit = 1, emulamos al metodo find
h2_uno_solo = soup.find_all('h2',limit=1)
print(h2_uno_solo)
     
# Podemos iterar sobre el objeto ya que con find_all obtenemos una lista, sobretodo para obtener el texto
for seccion in h2_todos:
  print(seccion.text) 

# get_text() para añadir más funcionalidades, strip por ejemplo es para quitar los huecos
for seccion in h2_todos:
  print(seccion.get_text(strip=True))
  
# UTILIZACION DE ATRIBUTOS, por ejemplo clase
divs = soup.find_all('div', class_ = "heading-container heading-center")

for div in divs:
  print(div)

# Todas las etiquetas que tengan el atributo "src", por ejemplo para obtener todas las imagenes .jpg
src_todos = soup.find_all(src=True)

for elemento in src_todos:
  if elemento['src'].endswith(".jpg"):
    print(elemento)

# @title Ejercicio: Bajar todas las imagenes!

url_imagenes = []

imagenes = soup.find_all(img=True)

for imagen in imagenes:

  if imagen['src'].endswith('png'):

    print(imagen['src'])
    r = requests.get(f"https://scrapepark.org/courses/spanish/{imagen['src']}")

    with open(f'imagen_{i}.png', 'wb') as f:
      f.write(r.content)
      
# TABLAS
soup.find_all('iframe')[0]['src']
     

# Información de tablas

URL_BASE = 'https://scrapepark.org/courses/spanish'
URL_TABLA = soup.find_all('iframe')[0]['src']

request_tabla = requests.get(f'{URL_BASE}/{URL_TABLA}')

html_tabla = request_tabla.text
soup_tabla = BeautifulSoup(html_tabla, "html.parser")
soup_tabla.find('table')

productos_faltantes = soup_tabla.find_all(['th', 'td'], attrs={'style':'color: red;'})
productos_faltantes = [talle.text for talle in productos_faltantes]

print(productos_faltantes)

divs = soup.find_all('div', class_='detail-box')
productos = []
precios = []

for div in divs:
  if (div.h6 is not None) and ('Patineta' in div.h5.text):
    producto = div.h5.get_text(strip=True)
    precio = div.h6.get_text(strip=True).replace('$', '')
    # Se puede agregar filtros
    print(f'producto: {producto:<16} | precio: {precio}')
    productos.append(producto)
    precios.append(precio)
    
# CAMBIOS QUE DEPENDEN DE LA URL

URL_BASE = "https://scrapepark.org/courses/spanish/contact"

for i in range(1,3):
  URL_FINAL = (f"{URL_BASE}{i}")
  print(URL_FINAL)
  r = requests.get(URL_FINAL)
  soup = BeautifulSoup(r.text, "html.parser")
  print(soup.h5.text)

# DATOS QUE NO SABEMOS DONDE SE ENCUENTRAN

# Expresiones regulares
import re

# 1. Obtener el HTML
URL_BASE = 'https://scrapepark.org/courses/spanish'
pedido_obtenido = requests.get(URL_BASE)
html_obtenido = pedido_obtenido.text

# 2. "Parsear" ese HTML
soup = BeautifulSoup(html_obtenido, "html.parser")

# RegExp para obtener los teléfonos
telefonos = soup.find_all(string=re.compile("\d+-\d+-\d+"))
print(telefonos)

# MOVIENDONOS POR EL ARBOL

copyrights = soup.find_all(string=re.compile("©"))
copyrights[0]

primer_copyright = copyrights[0]
primer_copyright.parent

# # Otro ejemplo con elementos al mismo nivel
menu = soup.find(string=re.compile("MENÚ"))
# menu.parent
menu.parent.find_next_siblings()
     
# COMENTARIO SOBRE EXCEPCIONES COMO AttributeError

strings_a_buscar = ["MENÚ", "©", "carpincho", "Patineta"]

for string in strings_a_buscar:
  try:
    resultado = soup.find(string=re.compile(string))
    print(resultado.text)
  except AttributeError:
    print(f"El string '{string}' no fue encontrado")
     
# ALMACENAMIENTO DE LOS DATOS, por ejemplo en csv

productos.insert(0, "productos")
precios.insert(0, "precios")
# datos = dict(zip(productos, precios))

datos = dict(zip(productos, precios)) 

datos.items()   

import csv

with open('datos.csv','w') as f:
    w = csv.writer(f)
    w.writerows(datos.items())