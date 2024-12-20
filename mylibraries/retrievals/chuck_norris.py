import requests
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='resources/general.log',
    level=logging.DEBUG,
    format='[%(asctime)s][%(levelname)s][%(filename)s][%(lineno)d] %(message)s'
)




class retrieve_chuck_norris_jokes:
    def __init__(self, categories_url):
        self.categories_url = categories_url
        self.chuck_norris_jokes = {}

    def retrieve_categories(self) -> list:
        try:
            response = requests.get(self.categories_url)
        except ConnectionError as e:
            print('Connection Error: ' + str(e))
            logger.error('Connection Error: ' + str(e))
        except Exception as e:
            print('unknonw error: ' + str(e))
            logger.error('unknonw error: ' + str(e))
        else:
            logger.debug('no error while trying response-testing')
            try:
                if response.status_code == 200:
                    categories = response.json()
            except Exception as e:
                print("unknown error occured while retrieving " + str(e))
                logger.critical("unknown error occured while retrieving " + str(e))
            else:
                return categories
    
    def update_jokes_from_categories(self):
        try:
            categories = self.retrieve_categories()
        except Exception as e:
            print("Unknmow error: " + str(e))
            logger.critical("Unknown execution error of self.retrieve_categories: " + str(e))
        else:
            logger.debug("Successfully retrieved categories in retrieve_jokes_from_categories()")
            
            try:
                for category in categories:
                    response = requests.get(f'https://api.chucknorris.io/jokes/random?category={category}')
                    self.chuck_norris_jokes[category] = response.json()
                    # first_time = 0
                    # if first_time <= 1:
                    #     logger.debug(response.json())
                    # first_time += 1
            except ConnectionError as e:
                print('Connection Error: ' + str(e))
                logger.error('Connection Error: ' + str(e))
            except Exception as e:
                print('unknonw error: ' + str(e))
                logger.error('unknonw error: ' + str(e))
            else:
                