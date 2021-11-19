import requests

from bs4 import BeautifulSoup


def data_extraction():
    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        date = soup.find('span', {'class': 'waktu'}).string.split(', ')
        time = date[1]

        earthquake_detail = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result_earthquake_detail = earthquake_detail.findChildren('li')

        result = dict()
        result['date'] = date[0]
        result['time'] = time
        result['magnitude'] = result_earthquake_detail[1].text
        result['depth'] = result_earthquake_detail[2].text
        result['location'] = result_earthquake_detail[3].text
        result['center'] = result_earthquake_detail[4].text
        result['feel'] = result_earthquake_detail[5].text

        return result
    else:
        return None


def show_data(result):
    if result is None:
        print("Tidak bisa menemukan data gempa terkini")
        return
    print('Last earthquake based on BMKG')
    print(f'Date: {result["date"]}')
    print(f'Time: {result["time"]}')
    print(f'Magnitude: {result["magnitude"]}')
    print(f'Depth: {result["depth"]}')
    print(f'Location : {result["location"]}')
    print(f'Center: {result["center"]}')
    print(f'Feel: {result["feel"]}')
