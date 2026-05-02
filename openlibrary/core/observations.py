"""Module for handling patron observation functionality"""

import requests

from infogami import config
from openlibrary import accounts
from . import cache

# URL for TheBestBookOn
TBBO_URL = config.get('tbbo_url')

def post_observation(data, s3_keys):
    headers = {
        'x-s3-access': s3_keys['access'],
        'x-s3-secret': s3_keys['secret']
    }

    response = requests.post(TBBO_URL + '/api/observations', data=data, headers=headers)

    return response.text

@cache.memoize(engine="memcache", key="tbbo_aspects", expires=config.get('tbbo_aspect_cache_duration'))
def get_aspects():
    response = requests.get(TBBO_URL + '/api/aspects')

    return response.text

def _sort_values(order_list, values_list):
    """Returns the names from values_list ordered by order_list.

    IDs in order_list that are not found in values_list are ignored.
    Values whose IDs are not in order_list are excluded.
    """
    name_by_id = {v['id']: v['name'] for v in values_list}
    return [name_by_id[i] for i in order_list if i in name_by_id]
