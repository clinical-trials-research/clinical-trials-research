from ctr import api


def test_get_studies() -> None:
    """
    Test API call to /studies.
    """
    api.get_studies(page_size=1)


def test_get_study_sizes() -> None:
    """
    Test API call to /stats/size.
    """
    api.get_study_sizes()


def test_get_field_values() -> None:
    """
    Test API call to /stats/field/values.
    """
    api.get_field_values()
