from collections import namedtuple

from ctr import api


def get_fields_to_piece():
    return {x["field"]: x["piece"] for x in api.get_field_values()}
