import requests
from pyfiglet import Figlet
import folium


def get_info_by_ip(ip='89.113.142.249'):
    try:
        responce = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        # print(responce)
        data = {
            '[IP]': responce.get('query'),
            '[Провайдер]': responce.get('isp'),
            '[Организация]': responce.get('org'),
            '[Страна]': responce.get('country'),
            '[Город]': responce.get('city'),
            '[Индекс]': responce.get('zip'),
            '[Долгота]': responce.get('lat'),
            '[Широта]': responce.get('lon')
        }

        for k, v in data.items():
            print(f'{k} : {v}')

        area = folium.Map(location=[responce.get('lat'), responce.get('lon')])
        area.save(f'{responce.get("query")}_{responce.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print('[!] Пожалуйста, проверьте подключение!')
    


def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP INFO'))
    ip = input('Введите [IP]: ')
    get_info_by_ip(ip=ip)



if __name__ == '__main__':
    main()