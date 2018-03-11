'''
Requests data from the weather api.

Http gzip compression should be enabled.
'''

import requests
import instance.config  # modify this once flask is set up *****


def dark_sky_call(
        key,
        latitude,
        longitude,
        options={'units': 'si', 'extend': 'hourly'},
        headers={'Accept-Encoding': 'gzip'}):

    call = (
        'https://api.darksky.net/forecast/' +
        instance.config.DARK_SKY_API_KEY + '/' +
        str(latitude) + ',' +
        str(longitude))

    return requests.get(call, params=options, headers=headers)


if __name__ == '__main__':
    r = dark_sky_call(
            instance.config.DARK_SKY_API_KEY,
            instance.config.LATITUDE,
            instance.config.LONGITUDE)

    print(r.url)
    print(r.text)
