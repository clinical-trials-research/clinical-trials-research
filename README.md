# Clinical Trials Research

## Installation

Create a virtual environment.

```bash
python -m venv .venv
```

Install

```bash
pip install -e '.[test,dev]'
```

## Notebooks

1. [Field Analysis](./notebooks/01-field-analysis.ipynb)
2. [Embedding Detailed Descriptions](./notebooks/02-embedding-detailed-descriptions.ipynb)

## Progress

- [ ] Literature Review
- [ ] `ctr` Utility Package
  - [x] Clincial Trials API.
  - [ ] Improve scripts to download data.
  - [ ] Display fields by piece instead of full name.
  - [ ] Remove `pydantic`?
- [ ] Field Analysis
  - [x] Flatten all fields.
  - [x] Extract fields data into a `DataFrame`.
  - [x] Display summary statistics of all non-string data.
  - [ ] Preprocess data more so that summary statistics make sense.
- [ ] Embed & Analyze "Detailed Description" Field.
  - [x] Preprocess data.
  - [ ] Embed "detailed description" field.
  - [ ] Clustering the embedded data.
  - [ ] Compare clusters with MeSH terms and keywords.

## Resources

- [Clinical Trials API](https://clinicaltrials.gov/data-api/api)
- [Clinical Trials Field Definitions](https://clinicaltrials.gov/data-api/about-api/study-data-structure)
