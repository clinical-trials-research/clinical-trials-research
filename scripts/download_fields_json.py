import json

import tqdm
from ctr import api

number_of_pages = (api.get_study_sizes().totalStudies // 1000) + 1
response = api.get_studies()
all_studies = response.studies

for _ in tqdm.trange(number_of_pages):
    try:
        if response.nextPageToken:
            response = api.get_studies(page_token=response.nextPageToken)
            all_studies.extend(response.studies)
        else:
            break
    except Exception as e:
        print(f"Encountered erorr {e}.")
        break

print("Finished downloading! Converting to JSON file...")
with open("fields.json", "w") as f:
    json.dump(all_studies, f, indent=4)
print("Done converting!")
