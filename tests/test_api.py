from ctr import api


def test_studies() -> None:
    """
    Test API call to /studies.
    """
    api.studies(page_size=1)


def test_stats_size() -> None:
    """
    Test API call to /stats/size.
    """
    api.stats_size()
