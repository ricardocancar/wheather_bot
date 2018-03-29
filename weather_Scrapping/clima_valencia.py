import requests
from bs4 import BeautifulSoup


def tiempo():
    page = requests.get(
        "https://freemeteo.es/eltiempo/valencia/tiempo-actual/ubicacion/?gid=2509954&station=2899&language=spanish&country=spain")

    soup = BeautifulSoup(page.content, 'html.parser')

    marco = soup.find(id="current-weather")
    forecast_item = marco.find_all(class_="last-renew-info")
    # print(forecast_item[0])

    today = forecast_item[0]

    period = today.find(class_='place').get_text()
    time = today.find(class_='temp').get_text()
    temp = today.find(class_='wind').get_text()

    stats = today.find(class_='stats').get_text()

    return period, time, temp, stats


if __name__ == '__main__':
    print("%s \n %s \n %s \n %s" % tiempo())
