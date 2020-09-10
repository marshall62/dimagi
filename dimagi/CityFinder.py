import requests

class CityFinder:
    #admincode1 is where state goes at two char abbrev
    api = "http://api.geonames.org/searchJSON?username=dimagi&password=dimagi&fuzzy=0.85"

    def get_correct_city (self, city, country, rec_list):
        if country:
            for r in rec_list:
                if r['countryName'] == country or r['countryCode'] == country :
                    return r

        return rec_list[0]

    def find_city_data(self, city, state, country):
        url= CityFinder.api + "&q=" + city
        if state:
            url += "&admin1="+state
        r = requests.get(url)
        json = r.json()
        if json.get('totalResultsCount',0) >= 1:
            recs = json['geonames']
            rec = self.get_correct_city(city, country, recs)
            return rec