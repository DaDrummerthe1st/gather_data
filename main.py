from datetime import datetime
import pytz
import logging

from mylibraries.retrievals.chuck_norris import retrieve_chuck_norris_jokes

categories = 'https://api.chucknorris.io/jokes/categories'
now_time = datetime.now(pytz.timezone('Europe/Stockholm'))

logger = logging.getLogger(__name__)

logging.basicConfig(
    filename='resources/general.log',
    level=logging.DEBUG,
    format='[%(asctime)s][%(levelname)s][%(filename)s][%(lineno)d] %(message)s'
)


chuck_norris1 = retrieve_chuck_norris_jokes(categories_url=categories)
chuck_norris1.retrieve_categories()
chuck_norris1.retrieve_jokes_from_categories()


