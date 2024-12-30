from os.path import exists

import requests
import logging
import pandas as pd
import sqlite3


logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='../../resources/general.log',
    level=logging.DEBUG,
    format='[%(asctime)s][%(levelname)s][%(filename)s][%(lineno)d] %(message)s'
)


class RetrieveChuckNorrisJokes:
    """Since there might be other sources to retrieve from"""
    def __init__(self, database_file):
        self.retrieved_df = ""

        # self.retrieved_joke_id = ""
        # self.retrieved_joke_created_at = ""
        # self.retrieved_joke_updated_at = ""
        # self.retrieved_joke_url = ""
        # self.retrieved_joke_value = ""
        # self.retrieved_joke_category = ""

        # self.joke_in_registry = 1

        # Database connection
        self.database_file = database_file
        self.connection_database = sqlite3.connect(self.database_file)
        try:
            self.connection_cursor = self.connection_database.cursor()
        except FileNotFoundError as e:
            print("FileNotFoundError: " + str(e))
        except sqlite3.OperationalError as e:
            print("sqlite3.OperationalError: " + str(e))
        else:
            print("connection cursor" + str(type(self.connection_cursor)))

    def retrieve_new_joke(self):
        """Fetching a random joke"""
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
            # print("response_json: " + str(response_json))
            # print("retrieved_df: " + str(self.retrieved_df))

            self.retrieved_df = pd.Series(response_json)
            # print("this is where the fun should be: " + str(self.retrieved_df))

            # self.retrieved_joke_id = response_json['id']
            # print("retrieved_joke_id: " + str(self.retrieved_joke_id))
            # print("retrieved_joke_id: " + str(response_json['id']))
            #
            # self.retrieved_joke_created_at = response_json['created_at']
            # self.retrieved_joke_updated_at = response_json['updated_at']
            # self.retrieved_joke_url = response_json['url']
            # self.retrieved_joke_value = response_json['value']
            # self.retrieved_joke_category = response_json['categories'] if response_json['categories'] != "" else ""
            # print("retrived category: " + str(self.retrieved_joke_category))

    # def check_for_existance(self):
    #     """This method does the following:
    #     - checks connection
    #     - searches database for retrieved joke id
    #     purpose is to return boolean regarding uniique ids
    #     """
    #     comparison = self.connection_cursor.execute(
    #       "select id from jokes where id=?",
    # (self.retrieved_joke_id,)
    #     ).fetchall()
    #
    #     try:
    #         if comparison == "":
    #             self.joke_in_registry = 1
    #             print("joke_in_registry: " + str(self.joke_in_registry))
    #         else:
    #             self.joke_in_registry = 0
    #             print("Joke NOT in registry: ", self.joke_in_registry)
    #             self.add_joke_to_database()
    #     except sqlite3.OperationalError as e:
    #         print("comparison, sqlite3.OperationalError: " + str(e))
    #     else:
    #         print("comparison: " + str(comparison))


    def add_joke_to_database(self):
        # print("is this joke in db? " + str(self.joke_in_registry))
        # if self.joke_in_registry == 0:
        #     try:
        #         self.retrieved_df.to_sql('jokes', self.connection_database, if_exists='fail')
        #     except ValueError as e:
        #         print("ValueError: %s", e)
        print("let's start here \n" + str(self.retrieved_df['created_at']))
        # for i in self.retrieved_df:
        #     print(i)
        try:
            self.connection_cursor.execute("""INSERT INTO jokes VALUES (?,?,?,?,?)""",
                                    (
                                        str(self.retrieved_df['id']),
                                        str(self.retrieved_df['created_at']),
                                        str(self.retrieved_df['updated_at']),
                                        str(self.retrieved_df['url']),
                                        str(self.retrieved_df['value'])
                                    )
                )

        except sqlite3.OperationalError as e:
            print("OperationalError: " + str(e))
        except sqlite3.ProgrammingError as e:
            print("ProgrammingError: " + str(e))

    def close_all_connections(self):
        self.connection_database.commit()

        self.connection_cursor.close()
        self.connection_database.close()

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


# categories = 'https://api.chucknorris.io/jokes/categories'
actual_path = "../../resources/database/chuck_norris_jokes.db"


chuck_norris1 = RetrieveChuckNorrisJokes(database_file=actual_path)
#chuck_norris1.retrieve_categories(categories_url=categories)
chuck_norris1.retrieve_new_joke()
#chuck_norris1.check_for_existance()
chuck_norris1.add_joke_to_database()

chuck_norris1.close_all_connections()
