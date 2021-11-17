"""
latest earthquake detection app
"""


def data_extraction():
    result = dict()
    result['date'] = '17 November 2021'
    result['time'] = '10:30:34 WIB'
    result['magnitude'] = 4.0
    result['location'] = {'ls': 1.48, 'bt': 134.01}
    result['center'] = 'The epicenter of the earthquake was in the sea 65 km southwest of North Bengkulu'
    result['feel'] = 'Felt (MMI Scale): III North Bengkulu, I-II Kepahiang, III Ketahun'

    return result


def show_data(result):
    print('Last earthquake based on BMKG')
    print(f'Date: {result["date"]}')
    print(f'Time: {result["time"]}')
    print(f'Magnitude: {result["magnitude"]}')
    print(f'Location : LS ={result["location"]["ls"]}, BT= {result["location"]["bt"]}')
    print(f'Center: {result["center"]}')
    print(f'Feel: {result["feel"]}')


if __name__ == '__main__':
    print('main application')
    result = data_extraction()
    show_data(result)
