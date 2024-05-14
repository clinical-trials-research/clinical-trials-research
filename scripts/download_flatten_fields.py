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


def save_fields(fields: dict, db):
    for key, value in fields.items():
        if key in db:
            db[key].extend(value)
        else:
            db[key] = value


def main():
    Path("./data/raw/fields").mkdir(parents=True, exist_ok=True)

    fields = defaultdict(list)
    number_of_pages = (api.get_study_sizes().totalStudies // 1000) + 1
    response = api.get_studies()

    batch_size = 100
    batch_count = 0

    with shelve.open("./fields/fields.shelf", writeback=True) as db:
        for _ in tqdm.trange(number_of_pages):
            for trial in response.studies:
                process_trial(fields, trial)

            batch_count += 1

            if batch_count >= batch_size:
                save_fields(fields, db)
                fields = defaultdict(list)
                batch_count = 0

            try:
                if response.nextPageToken:
                    response = api.get_studies(page_token=response.nextPageToken)
                else:
                    break
            except Exception as e:
                print(f"Encountered erorr {e}.")
                break

        if fields:
            save_fields(fields, db)

    print("Finished downloading! Storing data...")


if __name__ == "__main__":
    main()
