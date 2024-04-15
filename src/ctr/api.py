import httpx

from ctr.endpoints import StatsEndpoints, StudiesEndpoints
from ctr.response import StatsSizeResponse, StudiesResponse


def studies(*, page_size=1000, page_token="") -> StudiesResponse:
    """
    API call to /studies.

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
    return StudiesResponse(**response_json)


def stats_size() -> StatsSizeResponse:
    """
    API call to /stats/size.

    Returns:
        StatsSizeResponse: Pydantic model containing information on study sizes.
    """
    response_json = httpx.get(StatsEndpoints.STUDY_SIZES).json()
    return StatsSizeResponse(**response_json)
