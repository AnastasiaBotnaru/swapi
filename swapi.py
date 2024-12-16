from pathlib import Path
import requests


def save_sw_data():
    """Функция при помощи экземпляра класса SWRequester:
    1. получает полный список категорий SWAPI
    2. для каждой категории получает полное описание
    3. сохраняет информацию о категории в отдельном файле
    """
    request = SWRequester('https://swapi.dev/api')
    path = 'data'
    Path(path).mkdir(exist_ok=True)
    categories = request.get_sw_categories()  # Список категорий

    for item in categories:
        # Информация о категории в виде строки
        category_info = request.get_sw_info(item)
        file_name = item + '.txt'
        file_path = f'{path}/{file_name}'
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(category_info)


class APIRequester:
    """При инциализации класса в экземпляр сохраняется
    базовый URL некоторого API, например: https://swapi.dev.
    """

    def __init__(self, base_url):
        if base_url[-1] == '/':
            self.base_url = base_url[0:-1]
        else:
            self.base_url = base_url

    def get(self, relative_path=''):
        """Метод выполняет get-запрос к базовому URL экземпляра класса.
        Можно передать относительный URL в качестве необязательного параметра.
        Если при запросе возникает ошибка, метод выводит сообщение:
        'Возникла ошибка при выполнении запроса'.
        """
        if relative_path != '':
            url = f'{self.base_url}{relative_path}'
        else:
            url = f'{self.base_url}'
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except requests.RequestException:
            print('Возникла ошибка при выполнении запроса')
            return
        except requests.ConnectionError:
            print('Возникла ошибка при выполнении запроса')
            return
        except requests.HTTPError:
            print('Возникла ошибка при выполнении запроса')
            return
        except requests.Timeout:
            print('Возникла ошибка при выполнении запроса')
            return


class SWRequester(APIRequester):
    """Класс для доступа к списку категорий 'https://swapi.dev/api'."""

    def get_sw_categories(self):
        """Метод для получения списка категорий по URL 'https://swapi.dev/api'.
        """
        try:
            response = self.get(relative_path='/')
            response.raise_for_status()
            return response.json().keys()
        except requests.ConnectionError:
            return response
        except requests.HTTPError:
            return response
        except requests.RequestException as e:
            return e
        except requests.Timeout:
            return response

    def get_sw_info(self, sw_type):
        """Метод для получения полного описания конкретной категории по URL
        'https://swapi.dev/api/{название категории}'.
        """
        response = self.get(relative_path=f'/{sw_type}/')
        return response.text


save_sw_data()
