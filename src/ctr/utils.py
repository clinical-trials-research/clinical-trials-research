def normalize(data: dict, prefix: list[str] = []) -> dict:
    """
    Normalize a nested dictionary by flattening it.

    Args:
        data (dict): The dictionary to normalize
        prefix (list[str], optional): A list of strings representing the
                                      current path in the recursion. This
                                      is used internally.

    Returns:
        dict: Flattened dictionary.
    """
    flattened = {}
    for key, value in data.items():
        new_prefix = [*prefix, key]
        new_key = ".".join(new_prefix)
        match value:
            case dict():
                flattened |= normalize(value, new_prefix)
            case list() if all(isinstance(x, dict) for x in value):
                flattened[new_key] = [normalize(x, new_prefix) for x in value]
            case _:
                flattened[new_key] = value
    return flattened
