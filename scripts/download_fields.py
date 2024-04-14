import httpx
import pandas as pd
import tqdm

API_URL = "https://clinicaltrials.gov/api/v2"
GET_STUDIES_URL = API_URL + "/studies?pageSize=1000"
GET_STUDY_SIZES_URL = API_URL + "/stats/size"


# Get number of pages.
response_json = httpx.get(GET_STUDY_SIZES_URL).json()
total_studies = response_json.get("totalStudies")
pages = (total_studies // 1000) + 1

# Download fields.
response_json = httpx.get(GET_STUDIES_URL).json()
df = pd.json_normalize(response_json.get("studies"))

for _ in tqdm.trange(pages):
    try:
        next_page_token = response_json.get("nextPageToken")
        if next_page_token:
            response_json = httpx.get(
                GET_STUDIES_URL + f"&pageToken={next_page_token}"
            ).json()
            df = pd.concat(
                [df, pd.json_normalize(response_json["studies"])], ignore_index=True
            )
        else:
            break
    except Exception as e:
        print(f"Encountered erorr {e}.")
        break

print("Finished downloading! Converting to pickle file...")
df.to_pickle("./fields.pkl")
print("Done converting!")
