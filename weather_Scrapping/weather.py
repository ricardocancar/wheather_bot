import requests
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.WrohD9Zx200")

soup = BeautifulSoup(page.content, 'html.parser')

seven_day = soup.find(id="seven-day-forecast-container")
forecast_item = seven_day.find_all(class_="tombstone-container")
#print(forecast_item[0].prettify())
tonight = forecast_item[0]

period = tonight.find(class_='period-name').get_text()
time = tonight.find(class_='short-desc').get_text()
temp = tonight.find(class_='temp temp-high').get_text()

img = tonight.find('img')

print(period, '\n', time, '\n', temp)
print(img['title'])