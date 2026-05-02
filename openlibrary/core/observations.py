"""Module for handling patron observation functionality"""

import requests

from infogami import config
from openlibrary import accounts
from . import cache

# URL for TheBestBookOn
TBBO_URL = config.get('tbbo_url')


def _sort_values(order_list, values_list):
    """Return value names ordered exactly as in order_list.

    Given an ordered list of value IDs and a list of value dictionaries,
    returns the value names in the exact specified order.

    IDs present in order_list that are not found in values_list are ignored.
    Values whose IDs are not included in order_list are excluded.
    """
    values_by_id = {v['id']: v['name'] for v in values_list}
    return [values_by_id[id_] for id_ in order_list if id_ in values_by_id]

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
