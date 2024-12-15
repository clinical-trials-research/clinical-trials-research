API = "https://clinicaltrials.gov/api/v2"


class StudiesEndpoints:
    """
    Endpoints related to clinical trial studies.
    """

    STUDIES = API + "/studies?query.cond=cancer+OR+cancers+OR+cancerous+OR+tumor+OR+carcinoma+OR+carcinogen+OR+chemo+OR+chemotherapy+OR+chrondosarcoma+OR+adenocarcinoma+OR+adenoma+OR+lymphoma+OR+leiomyoma+OR+leukemia+OR+lumpectomy+OR+macroglobulinemia+OR+melanoma+OR+metastasis+OR+micrometastases+OR+metastatic+OR+metastasize+OR+myeloma+OR+oncogenes+OR+oncologist+OR+oncology+OR+osteosarcoma+OR+radiation+therapy+OR+sarcoma&query.term=AREA%5BCompletionDate%5DRANGE%5B2019-01-01%2CMAX%5D&countTotal=true&pageSize=1000"


class StatsEndpoints:
    """
    Endpoints related to data statistics.
    """

    STUDY_SIZES = API + "/stats/size"
    FIELD_VALUES = API + "/stats/field/values"
