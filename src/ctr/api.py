import httpx

from ctr.endpoints import StatsEndpoints, StudiesEndpoints
from ctr.response import GetStudiesResponse, GetStudySizesResponse


def get_studies(*, page_size: int = 1000, page_token: str = "") -> GetStudiesResponse:
    """
    API call to /studies.

    Retrieves a list of studies that contains their respective fields.

    Args:
        page_size (int, optional): The number of pages to retrieve. Defaults to 1000.
        page_token (str, optional): Allows to get the next page. Defaults to "".

    Returns:
        StudiesResponse: Pydantic model containing studies and next page token.
    """
    params = {"pageSize": str(page_size)}
    if page_token:
        params.update({"pageToken": page_token})

    response = httpx.get(StudiesEndpoints.STUDIES, params=params)
    response.raise_for_status()
    return GetStudiesResponse(**response.json())


def get_study_sizes() -> GetStudySizesResponse:
    """
    API call to /stats/size.

    Gives information about the total number of studies and the size (bytes) of stuides.

    Returns:
        StatsSizeResponse: Pydantic model containing information on study sizes.
    """
    response_json = httpx.get(StatsEndpoints.STUDY_SIZES).json()
    return GetStudySizesResponse(**response_json)


def get_field_values(types: list[str] = [], fields: list[str] = []) -> list[dict]:
    """
    API call to /stats/field/values.

    Retrieves information about individual fields.

    Args:
        types (List[str]): List of types to include in the query.
        fields (List[str]): List of fields to include in the query.

    Returns:
        List[Dict]: JSON response from the API as a list of dictionaries.
    """
    params = {}
    if types:
        params.update({"types": "|".join(types)})
    if fields:
        params.update({"fields": "|".join(fields)})

    response = httpx.get(StatsEndpoints.FIELD_VALUES, params=params)
    response.raise_for_status()
    return response.json()
