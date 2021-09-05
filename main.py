import requests
import json

URL = 'https://en.wikipedia.org/wiki/'
response = requests.get(URL)
response.raise_for_status()
with open('countries.json') as file:
    countries = file.read()

countries_list = json.loads(countries)
for dict in countries_list:
    countries_name = dict['name']['common'].replace(' ', '_')
    # print(countries_name, '-', URL + countries_name)


class Wiki:

    def __init__(self, country, start):
        self.file = open(country, encoding='UTF-8')
        self.start = start - 1
        self.country_list = json.load(self.file)


    def __iter__(self):
        return self

    def __next__(self):
      country_dict = {}
      self.start += 1
      if self.start > len(self.country_list):
          raise StopIteration

      country_name = self.country_list[self.start]['name']['common'].replace(' ', '_')
      country_link = URL + country_name
      country_dict[country_name] = country_link
      return country_dict

my_list = Wiki('countries.json', 0)
with open('wiki', 'w', encoding='UTF-8') as file:
    for elm in my_list:
        json.dump(elm, file, ensure_ascii=False, indent=2)





