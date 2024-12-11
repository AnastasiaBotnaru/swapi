import os
import requests


def save_sw_data(url):
    category_info_request = SWRequester(url)
    os.makedirs('data', exist_ok=True)
    categories = category_info_request.get_sw_categories()  # Список категорий

    for item in categories:
        # Информация о категории в виде строки
        category_info = category_info_request.get_sw_info(item)
        file_name = item + '.txt'
        file_path = 'data/' + file_name
        with open(file_path, 'w') as file:
            file.write(category_info)


class APIRequester:
    def __init__(self, base_url):
        if base_url[-1] != '/':
            self.base_url = base_url + '/'
        else:
            self.base_url = base_url

    def get(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except requests.ConnectionError:
            return response
        except requests.HTTPError:
            return response
        except requests.RequestException:
            return response
        except requests.Timeout:
            return response


class SWRequester(APIRequester):
    def get_sw_categories(self):
        response = self.get(self.base_url)
        categories = []
        for item in response.json().keys():
            categories.append(item)
        return categories

    def get_sw_info(self, sw_type):
        category_info_url = self.base_url + sw_type + '/'
        response = self.get(category_info_url)
        return response.text


# m = APIRequester('https://swapi.dev/api/planets/1/')
# print(m.get())
# cat = SWRequester('https://swapi.dev/api/')
# print(cat.get_sw_categories())  # Возвращает список
# print(type(cat.get_sw_categories()))
# print(cat.get_sw_info('people'))  # Возвращает строку
# print(type(cat.get_sw_info('people')))

save_sw_data('https://swapi.dev/api/')
