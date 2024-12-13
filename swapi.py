from pathlib import Path
import requests


def save_sw_data():
    request = SWRequester('https://swapi.dev/api')
    path = 'data'
    Path(path).mkdir(exist_ok=True)
    categories = request.get_sw_categories()  # Список категорий

    # for item in categories_dict.keys():
        #     categories.append(item)
        # categories.sort()
        # return categories

    for item in categories:
        # Информация о категории в виде строки
        category_info = request.get_sw_info(item)
        file_name = item + '.txt'
        file_path = f'{path}/{file_name}'
        with open(file_path, 'w') as file:
            file.write(category_info)


class APIRequester:
    def __init__(self, base_url): # Базовый URL для swapi - это https://swapi.dev/
        if base_url[-1] == '/':
            self.base_url = base_url[0:-1]
        else:
            self.base_url = base_url

    def get(self, relative_path=''):
        if relative_path != '':
            url = f'{self.base_url}{relative_path}'
        else:
            url = f'{self.base_url}'    
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            return e
        except requests.ConnectionError:
            return response
        except requests.HTTPError:
            return response
        except requests.Timeout:
            return response
        # except requests.RequestException as e:
        #     return e


class SWRequester(APIRequester):

    def get_sw_categories(self):
        """Попробовать добавить проверку на код 200 и только в этом случае
        пытаться получить json"""
        # categories_dict = {}
        # categories = []
        try:
            response = self.get(relative_path='/')
            response.raise_for_status()
            # categories_dict = response.json()
            return response.json().keys()
        except requests.ConnectionError:
            return response
        except requests.HTTPError:
            return response
        except requests.RequestException as e:
            return e
        except requests.Timeout:
            return response

        # for item in categories_dict.keys():
        #     categories.append(item)
        # categories.sort()
        # return categories

    def get_sw_info(self, sw_type):
        response = self.get(relative_path=f'/{sw_type}/')
        return response.text


# m = APIRequester('https://swapi.dev/api/planets/1/')
# print(m.get())
# cat = SWRequester('https://swapi.dev/api/')
# print(cat.get_sw_categories())  # Возвращает список
# print(type(cat.get_sw_categories()))
# print(cat.get_sw_info('people'))  # Возвращает строку
# print(type(cat.get_sw_info('people')))


save_sw_data()

# print(m.base_url)
# print(m.url)
# print('-' * 5)
# print(m.get_sw_categories())
