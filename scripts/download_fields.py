import httpx
import pandas as pd
import tqdm

API_URL = "https://clinicaltrials.gov/api/v2/studies?pageSize=1000"
PAGES = 491

response_json = httpx.get(API_URL).json()
df = pd.json_normalize(response_json.get("studies"))

# In order to display a progress bar, I need to manually set the number of interations as 492.
for _ in tqdm.trange(PAGES):
    try:
        next_page_token = response_json.get("nextPageToken")
        if next_page_token:
            response_json = httpx.get(API_URL + f"&pageToken={next_page_token}").json()
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
