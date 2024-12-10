import requests


class APIRequester:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self):
        try:
            response = requests.get(self.base_url)
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


m = APIRequester('https://swapi.dev/api/planets/1/')
print(m.get())