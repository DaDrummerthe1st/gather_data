import requests
import logging
import pandas as pd


logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='resources/general.log',
    level=logging.DEBUG,
    format='[%(asctime)s][%(levelname)s][%(filename)s][%(lineno)d] %(message)s'
)


class RetrieveChuckNorrisJokes:
    """Since there might be other sources to retrieve from"""
    def __init__(self):
        # self.categories_url = ""
        self.chuck_norris_jokes = {
            "id": [],
            "created_at": [],
            "updated_at": [],
            "value": [],
            "category": []
        }
        self.pd = pd.DataFrame(self.chuck_norris_jokes)

    def retrieve_new_joke(self):
        """
        By ranomdly fetching a joke and then testing it,
        fills up the database with new Chuck Norris jokes
        """
        print(self.chuck_norris_jokes)
        try:
            response = requests.get(
                'https://api.chucknorris.io/jokes/random', timeout=10)
            response_json = response.json()
        except KeyError as key_err:
            print("Key Error: %s", key_err)
            logger.critical("Key Error: %s", key_err)
        except ConnectionError as e:
            print("Connection Error: %s", e)
            logger.error("Connection Error: %s", e)
        else:
            # print(self.pd["id"])
            print(response_json)
            try:
                response_df = pd.DataFrame(response_json)
                print(response_df + "is the answer")
            except ValueError as val_err:
                print("ValueError: " + str(val_err))
            else:
                for joke_id in self.pd["id"]:
                    # print(joke_id)
                    # print(response_df)
                    if response_df["id"] != joke_id:
                        print("this joke is not found in the database")
                        # self.pd["id"] = self.pd[id]
                        # self.pd[""]

    # def retrieve_categories(self, categories_url) -> list:
    #     """UNUSED
    #     This method retrieves all the available categories
    #     """
    #     self.categories_url = categories_url
    #     try:
    #         response = requests.get(categories_url, timeout=10)
    #     except ConnectionError as e:
    #         print('Connection Error: ' + str(e))
    #         logger.critical("Connection Error: %s", e)
    #     else:
    #         logger.debug("no error while trying response-testing")
    #         try:
    #             if response.status_code == 200:
    #                 categories = response.json()
    #         except TypeError as e:
    #             print('Connection Error: ' + str(e))
    #             logger.critical("Connection Error: %s", e)
    #         else:
    #             return categories

    # def update_jokes_from_categories(self):
    #     """DEPRECATED
    #     When categories are found this method retrieves one joke from each category
    #     """
    #     try:
    #         categories = self.retrieve_categories(self.categories_url)
    #     except TypeError as e:
    #         print("TypeError: " + str(e))
    #         logger.critical("TypeError: %s", e)
    #     else:
    #         logger.debug(
    #             "Successfully retrieved categories in retrieve_jokes_from_categories()")

    #         try:
    #             for category in categories:
    #                 response = requests.get(
    #                     f'https://api.chucknorris.io/jokes/random?category={
    #                         category}',
    #                     timeout=10
    #                 )
    #                 response_json = response.json()
    #                 for category in response_json["categories"]:
    #                     print(category)

    #                 # self.chuck_norris_jokes.append(response.json())
    #                 # first_time = 0
    #                 # if first_time <= 1:
    #                 #     logger.debug(response.json())
    #                 # first_time += 1
    #         except KeyError as key_err:
    #             print("Key Error: " + str(key_err))
    #             logger.critical("Key Error: %s", key_err)
    #         except ConnectionError as e:
    #             print("Connection Error: %s", e)
    #             logger.error("Connection Error: %s", e)
    #         else:
    #             print(self.chuck_norris_jokes)


categories = 'https://api.chucknorris.io/jokes/categories'

chuck_norris1 = RetrieveChuckNorrisJokes
#chuck_norris1.retrieve_categories(categories_url=categories)
chuck_norris1.retrieve_new_joke()
