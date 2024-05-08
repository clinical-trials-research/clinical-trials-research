import shelve
from collections import defaultdict
from pathlib import Path

import tqdm
from ctr import api


def process_trial(fields: defaultdict, data: dict, prefix=[]) -> None:
    for key, value in data.items():
        if isinstance(value, dict):
            process_trial(fields, value, prefix + [key])
        elif isinstance(value, list) and all(isinstance(x, dict) for x in value):
            for nested in value:
                process_trial(fields, nested, prefix + [key])
        else:
            name = ".".join(prefix + [key])
            fields[name].append(value)


def main():
    fields = defaultdict(list)
    number_of_pages = (api.get_study_sizes().totalStudies // 1000) + 1
    response = api.get_studies()

    fields_dir = Path("./fields")
    if not fields_dir.exists():
        fields_dir.mkdir(parents=True, exist_ok=True)
        print("Created /fields to store data files.")

    for _ in tqdm.trange(number_of_pages):
        for trial in response.studies:
            process_trial(fields, trial)
        try:
            if response.nextPageToken:
                response = api.get_studies(page_token=response.nextPageToken)
            else:
                break
        except Exception as e:
            print(f"Encountered erorr {e}.")
            break

    print("Finished downloading! Storing data...")
    with shelve.open("./fields/fields.shelf") as db:
        for key, value in fields.items():
            db[key] = value
    print("Done storing!")


if __name__ == "__main__":
    main()
