"""
latest earthquake detection app
"""
import bmkg_recent_earthquake

if __name__ == '__main__':
    print('result scraping :\n')
    result = bmkg_recent_earthquake.data_extraction()
    bmkg_recent_earthquake.show_data(result)
