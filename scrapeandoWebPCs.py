from bs4 import BeautifulSoup
import bs4
import requests

url = "https://www.elindependiente.com/de-tiendas/2024/02/27/mejores-ordenadores-gaming/"
# En console>navigator.userAgent encontramos esta firma nuestra, se puede falsificar en developers.google.com
# luego nos iremos a rastreadores y en rastreadores habituales podemos usar el googlebot para ordenadores
headers = "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/W.X.Y.Z Safari/537.36"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Vamos a obtener los nombres y links de compra para los 5 mejores portatiles y el enlace a su compra
    nombre = soup.find_all("h3", limit = 5)
    if nombre:
        for i in nombre:
            nombre_text = i.text
            enlace = i.find("a")
            print(f"El nombre del PC es: {nombre_text} \n El enlace a su compra: {enlace.get("href")} \n")

