from pydantic import BaseModel


class GetStudiesResponse(BaseModel):
    """
    Response from /studies.
    """

    studies: list
    nextPageToken: str


class GetStudySizesResponse(BaseModel):
    """
    Response from /stats/size.
    """

    totalStudies: int
    averageSizeBytes: int
    percentiles: dict


class GetFieldValuesResponse(BaseModel):
    """
    Response from /stats/field/values.
    """
