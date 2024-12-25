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
        # self.categories_url = ""
        # self.chuck_norris_jokes = {
        #     "id": [],
        #     "created_at": [],
        #     "updated_at": [],
        #     "value": [],
        #     "category": []
        # }

        self.retrieved_df = ""

        self.retrieved_joke_id = ""
        self.retrieved_joke_created_at = ""
        self.retrieved_joke_updated_at = ""
        self.retrieved_joke_url = ""
        self.retrieved_joke_value = ""
        self.retrieved_joke_category = ""

        self.does_exist_or_not = ""

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

    def check_for_existance(self):
        """This method does the following:
        - checks connection
        - searches database for retrieved joke id
        purpose is to return boolean regarding uniique ids
        """
        comaparison = self.connection_cursor.execute("select id from jokes where id=?", (self.retrieved_joke_id,)).fetchall()
        if not comaparison:

        print ("here it is")
       #(Tkw1X2aESzCyrjqeSTG-RA', '2020-01-05 13:42:25.905626', '2020-01-05 13:42:25.905626', 'https://api.chucknorris.io/jokes/Tkw1X2aESzCyrjqeSTG-RA', 'Chuck Norris has a new policy regarding gays in the military. Dont ask - EVER!')""")
        # self.connection_cursor.execute('insert into jokes values (?, ?, ?, ?)', (Tkw1X2aESzCyrjqeSTG-RA', '2020-01-05 13:42:25.905626', '2020-01-05 13:42:25.905626', 'https://api.chucknorris.io/jokes/Tkw1X2aESzCyrjqeSTG-RA', 'Chuck Norris has a new policy regarding gays in the military. Dont ask - EVER!')""")

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
            self.retrieved_df = pd.DataFrame(response_json)
            self.retrieved_joke_id = response_json['id']
            print(self.retrieved_joke_id)
            self.retrieved_joke_created_at = response_json['created_at']
            self.retrieved_joke_updated_at = response_json['updated_at']
            self.retrieved_joke_url = response_json['url']
            self.retrieved_joke_value = response_json['value']
            #self.retrieved_joke_category = response_json['category']

    def add_joke_to_database(self):
        pass

    def close_all_connections(self):
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
chuck_norris1.check_for_existance()

chuck_norris1.close_all_connections()
