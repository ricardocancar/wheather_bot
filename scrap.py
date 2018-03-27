import requests
from bs4 import BeautifulSoup
##obtiene el codigo html
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
## recibe el status codigo
# print(page.status_code)

soup = BeautifulSoup(page.content, "html.parser")
# print(soup.prettify())

# print(list(soup.children))


# print([type(item) for item in list(soup.children)])


#print(soup.find_all('p')[0].get_text())
###### find_all  devuelve una lista asi que para obtener el texto, utilizamos el comando get text

#print(soup.find('p'))
