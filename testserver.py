from http import HTTPStatus
from http.server import BaseHTTPRequestHandler
import socketserver

PORT = 8000


class CustomHandler(BaseHTTPRequestHandler):
    """docstring for CustomHandler"""

    def __init__(self, *a, **kw):
        super(CustomHandler, self).__init__(*a, **kw)

    def do_GET(self):
        print(self.path)
        if 'location/search' in self.path:
            response = '[{"title":"London","location_type":"City","woeid":44418,"latt_long":"51.506321,-0.12714"}]'
        else:
            response = '{"consolidated_weather":[{"id":5117815038148608,"weather_state_name":"Heavy Cloud","weather_state_abbr":"hc","wind_direction_compass":"N","created":"2019-11-29T18:16:02.246168Z","applicable_date":"2019-11-29","min_temp":2.5999999999999996,"max_temp":7.105,"the_temp":7.21,"wind_speed":3.286602792637663,"wind_direction":353.5,"air_pressure":1017.0,"humidity":74,"visibility":6.701798993875765,"predictability":71},{"id":5271251402620928,"weather_state_name":"Heavy Cloud","weather_state_abbr":"hc","wind_direction_compass":"E","created":"2019-11-29T18:16:02.325410Z","applicable_date":"2019-11-30","min_temp":2.18,"max_temp":7.515000000000001,"the_temp":7.37,"wind_speed":5.047240495564569,"wind_direction":89.32250598939655,"air_pressure":1021.0,"humidity":78,"visibility":7.332180068400541,"predictability":71},{"id":6473117536878592,"weather_state_name":"Heavy Cloud","weather_state_abbr":"hc","wind_direction_compass":"NNE","created":"2019-11-29T18:16:02.119701Z","applicable_date":"2019-12-01","min_temp":2.73,"max_temp":6.915,"the_temp":6.925,"wind_speed":8.005976402958721,"wind_direction":28.161765540879486,"air_pressure":1022.5,"humidity":72,"visibility":11.112291716376362,"predictability":71},{"id":6630514062524416,"weather_state_name":"Clear","weather_state_abbr":"c","wind_direction_compass":"NW","created":"2019-11-29T18:16:02.233838Z","applicable_date":"2019-12-02","min_temp":0.81,"max_temp":6.05,"the_temp":5.715,"wind_speed":3.795200901232801,"wind_direction":321.30730021345533,"air_pressure":1031.5,"humidity":73,"visibility":13.919336077308518,"predictability":68},{"id":5465194710958080,"weather_state_name":"Light Cloud","weather_state_abbr":"lc","wind_direction_compass":"WSW","created":"2019-11-29T18:16:03.417728Z","applicable_date":"2019-12-03","min_temp":0.665,"max_temp":6.109999999999999,"the_temp":5.445,"wind_speed":1.8298513115220445,"wind_direction":241.50650145719482,"air_pressure":1030.0,"humidity":81,"visibility":5.310238208860256,"predictability":70},{"id":6397151309463552,"weather_state_name":"Clear","weather_state_abbr":"c","wind_direction_compass":"NW","created":"2019-11-29T18:16:04.531582Z","applicable_date":"2019-12-04","min_temp":0.4850000000000001,"max_temp":6.155,"the_temp":5.62,"wind_speed":1.3803952914976536,"wind_direction":318.5,"air_pressure":1024.0,"humidity":76,"visibility":9.999726596675416,"predictability":68}],"time":"2019-11-29T18:54:57.577122Z","sun_rise":"2019-11-29T07:40:26.580829Z","sun_set":"2019-11-29T15:56:34.639557Z","timezone_name":"LMT","parent":{"title":"England","location_type":"Region / State / Province","woeid":24554868,"latt_long":"52.883560,-1.974060"},"sources":[{"title":"BBC","slug":"bbc","url":"http://www.bbc.co.uk/weather/","crawl_rate":360},{"title":"Forecast.io","slug":"forecast-io","url":"http://forecast.io/","crawl_rate":480},{"title":"HAMweather","slug":"hamweather","url":"http://www.hamweather.com/","crawl_rate":360},{"title":"Met Office","slug":"met-office","url":"http://www.metoffice.gov.uk/","crawl_rate":180},{"title":"OpenWeatherMap","slug":"openweathermap","url":"http://openweathermap.org/","crawl_rate":360},{"title":"Weather Underground","slug":"wunderground","url":"https://www.wunderground.com/?apiref=fc30dc3cd224e19b","crawl_rate":720},{"title":"World Weather Online","slug":"world-weather-online","url":"http://www.worldweatheronline.com/","crawl_rate":360}],"title":"London","location_type":"City","woeid":44418,"latt_long":"51.506321,-0.12714","timezone":"Europe/London"}'
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(response.encode())
        return


def main():
    Handler = CustomHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"serving at port {PORT}")
        httpd.serve_forever()


if __name__ == '__main__':
    main()
