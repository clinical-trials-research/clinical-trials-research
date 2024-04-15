from pydantic import BaseModel


class StudiesResponse(BaseModel):
    """
    Response from /studies.
    """

    studies: list
    nextPageToken: str


class StatsSizeResponse(BaseModel):
    """
    Response from /stats/size.
    """

    totalStudies: int
    averageSizeBytes: int
    percentiles: dict
