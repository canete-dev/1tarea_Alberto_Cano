# Importamos beautifulSoup, bs4 y requests
from bs4 import BeautifulSoup
import requests
import bs4

# Comprobamos las versiones para ver que esta todo correcto
print("Version de BeautifulSoup:", bs4.__version__)
print("Version de requests:", requests.__version__)

# Creamos una variable a la que le pasamos la url de la pagina que queremos scrapear
url = "http://127.0.0.1:5500/holaMundo.html"
# Creamos una variable que va a almacenar la peticion de tipo get
request = requests.get(url)
# Creamos un variable que almacene el contenido de la peticion
htmlScrapeado = request.content
# Creamos un variable que va a 
soup = BeautifulSoup(htmlScrapeado, "html.parser")
print(soup)

h1 = soup.find("h1")
print(h1)