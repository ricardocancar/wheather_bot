import requests
from bs4 import BeautifulSoup
##obtiene el codigo html
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
## si el código recibido es 200, la pagina fue cargada correctamente.  
# print(page.status_code)

soup = BeautifulSoup(page.content, "html.parser")
# print(soup.prettify())

# print(list(soup.children))

#(muesta los diferentes objetos que conforman el metodo soup)
# print([type(item) for item in list(soup.children)])


#print(soup.find_all('p')[0].get_text())
###### find_all  devuelve una lista asi que para obtener el texto, utilizamos el comando get text

#print(soup.find('p'))
