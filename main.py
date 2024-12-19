import requests
from datetime import datetime
import pytz

categories = 'https://api.chucknorris.io/jokes/categories'
now_time = datetime.now(pytz.timezone('Europe/Stockholm'))


class retrieve_chuck_norris_jokes:
    def __init__(self, categories_url):
        self.categories_url = categories_url

    def retrieve_categories(self):
        try:
            response = requests.get(self.categories_url)
        except ConnectionError as e:
            print('Connection Error: ' + str(e))
        except Exception as e:
            print('unknonw error: ' + str(e))
        else:
            if response.status_code == 200:
                data = response.json()
                print(data)



chuck_norris1 = retrieve_chuck_norris_jokes(categories)
chuck_norris1.retrieve_categories()


