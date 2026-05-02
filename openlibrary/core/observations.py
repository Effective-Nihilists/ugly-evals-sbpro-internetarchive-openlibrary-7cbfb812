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
    """
    Return value names ordered according to order_list.

    - Returns names in the exact order specified by order_list.
    - Ignores IDs in order_list not found in values_list (no errors).
    - Excludes values whose IDs are not in order_list.
    """
    value_map = {v['id']: v['name'] for v in values_list}
    return [value_map[oid] for oid in order_list if oid in value_map]
