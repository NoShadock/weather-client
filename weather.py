# weather API client: https://www.metaweather.com/api/
import requests

base_url = 'https://www.metaweather.com/api'
# base_url = 'http://localhost:8000'  # test url


def get(url, base_url=base_url, **kw):
    r = requests.get(url=f'{base_url}/{url}', **kw)
    return r.json()


def weather(woeid):
    forecasts = get(url=f'location/{woeid}')['consolidated_weather']
    tomorrow = forecasts[1]
    return tomorrow['weather_state_name']


def locationQuery(query):
    return get(url='location/search', params={'query': query})


def locationLattLong(lattitude, longitude):
    return get(url='location/search', params={'lattlong': f'{lattitude},{longitude}'})


def lookup(location):
    data = get(url='+'.join(location), base_url='https://geocode.xyz', params={'json': 1})
    return [data['latt'], data['longt']]


def main(args):
    if args.location:
        try:
            location = locationQuery(' '.join(args.location))[0]
        except IndexError:
            print('No corresponding location, looking up GPS coordinates for closest point.')
            args.gps = lookup(args.location)
            args.location = None
            return main(args)
    else:
        location = locationLattLong(*args.gps)[0]
        print(f'The closest weather forecast is for {location["title"]} ({location["location_type"]})')
    print(weather(location['woeid']))


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                     description='''wheather.com API client
For any given location, return tomorrow's weather forecast.
If a location is unknown in the forecast network, lookup the closest one.''',)
    location_format = parser.add_mutually_exclusive_group(required=True)
    location_format.add_argument('--location', type=str, help='address or city name', nargs='+')
    location_format.add_argument('--gps', metavar='L', type=float,
                                 help='lattitude longitude', nargs=2)
    args = parser.parse_args()
    main(args)
