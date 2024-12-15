from pydantic import BaseModel
from typing import List, Optional

class GetStudiesResponse(BaseModel):
    """
    Response from /studies.
    """

    totalCount: Optional[int] = 0
    studies: list
    nextPageToken: Optional[str] = ""


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
