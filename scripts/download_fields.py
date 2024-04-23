import pandas as pd
import tqdm
from ctr import api

number_of_pages = (api.get_study_sizes().totalStudies // 1000) + 1
response = api.get_studies()
df = pd.json_normalize(response.studies)

for _ in tqdm.trange(number_of_pages):
    try:
        if response.nextPageToken:
            response = api.get_studies(page_token=response.nextPageToken)
            df = pd.concat([df, pd.json_normalize(response.studies)], ignore_index=True)
        else:
            break
    except Exception as e:
        print(f"Encountered erorr {e}.")
        break

print("Finished downloading! Converting to pickle file...")
df.to_pickle("./field.pkl")
print("Done converting!")
