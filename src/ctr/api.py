import httpx

from ctr.endpoints import StatsEndpoints, StudiesEndpoints
from ctr.response import GetStudiesResponse, GetStudySizesResponse


def get_studies(*, page_size=1000, page_token="") -> GetStudiesResponse:
    """
    API call to /studies.

    Retrieves a list of studies that contains their respective fields.

    Args:
        page_size (int, optional): The number of pages to retrieve. Defaults to 1000.
        page_token (str, optional): Allows to get the next page. Defaults to "".

    Returns:
        StudiesResponse: Pydantic model containing studies and next page token.
    """
    URL = StudiesEndpoints.STUDIES + f"?pageSize={page_size}"
    if page_token:
        URL += f"&pageToken={page_token}"
    response_json = httpx.get(URL).json()
    return GetStudiesResponse(**response_json)


def get_study_sizes() -> GetStudySizesResponse:
    """
    API call to /stats/size.

    Gives information about the total number of studies and the size (bytes) of stuides.

    Returns:
        StatsSizeResponse: Pydantic model containing information on study sizes.
    """
    response_json = httpx.get(StatsEndpoints.STUDY_SIZES).json()
    return GetStudySizesResponse(**response_json)


def get_field_values() -> list[dict]:
    """
    API call to /stats/field/values.

    Retrieves information about individual fields.

    Returns:
        list: _description_
    """
    response_json = httpx.get(StatsEndpoints.FIELD_VALUES).json()
    return response_json
