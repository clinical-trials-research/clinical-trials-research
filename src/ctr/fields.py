from collections import namedtuple

from ctr import api



def get_fields():
    fields = {}
    for field in api.get_field_values():
        fields[field["piece"]] = field["field"]

    Fields = namedtuple("Fields", fields)
    return Fields(**fields)
