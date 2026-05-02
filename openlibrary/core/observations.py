"""Module for handling patron observation functionality"""

import requests

from infogami import config
from openlibrary import accounts
from . import cache

# URL for TheBestBookOn
TBBO_URL = config.get('tbbo_url')


def _sort_values(order_list, values_list):
    """Return value names in the order specified by order_list.

    Args:
        order_list: List of IDs specifying desired display order
        values_list: List of dicts with 'id' and 'name' keys

    Returns:
        List of names ordered according to order_list. IDs in order_list
        that don't exist in values_list are ignored. Values whose IDs
        are not in order_list are excluded.
    """
    id_to_name = {v['id']: v['name'] for v in values_list}
    return [id_to_name[id] for id in order_list if id in id_to_name]

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
