API = "https://clinicaltrials.gov/api/v2"


class StudiesEndpoints:
    """
    Endpoints related to clinical trial studies.
    """

    STUDIES = API + "/studies"


class StatsEndpoints:
    """
    Endpoints related to data statistics.
    """

    STUDY_SIZES = API + "/stats/size"
    FIELD_VALUES = API + "/stats/field/values"
