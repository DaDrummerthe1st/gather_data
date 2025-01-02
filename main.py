from datetime import datetime
import pytz
import logging

from mylibraries.retrievals.chuck_norris import RetrieveChuckNorrisJokes

categories = 'https://api.chucknorris.io/jokes/categories'
now_time = datetime.now(pytz.timezone('Europe/Stockholm'))

logger = logging.getLogger(__name__)


logging.basicConfig(
    filename='resources/general.log',
    level=logging.DEBUG,
    format='[%(asctime)s][%(levelname)s][%(filename)s][%(lineno)d] %(message)s'
)

actual_path = "resources/database/chuck_norris_jokes.db"

chuck_norris1 = RetrieveChuckNorrisJokes(database_file=actual_path)
#chuck_norris1.retrieve_categories(categories_url=categories)
for i in range(0, 100):
    chuck_norris1.retrieve_new_joke()
    chuck_norris1.check_for_joke_in_database()
    chuck_norris1.crud_chuck_norris()
    print(f"succesfully run iteration {i}")

chuck_norris1.close_all_connections()



