# Clinical Trials Research

## Notebooks

1. [Field Analysis](./notebooks/01-field-analysis.ipynb)
2. [Embedding Detailed Descriptions](./notebooks/02-embedding-detailed-descriptions.ipynb)

## Installation

Create a virtual environment.

```bash
python -m venv .venv
```

Install

```bash
pip install -e '.[test,dev]'
```

## Progress

- [ ] Literature Review
- [ ] Field Analysis
  - [x] Extract fields data into a `DataFrame`.
  - [ ] Deal with nested data in fields.
  - [ ] Display summary statistics of all data.
- [ ] Embed & Analyze "Detailed Description Field.

## Resources

- [Clinical Trials API](https://clinicaltrials.gov/data-api/api)
- [Clinical Trials Field Definitions](https://clinicaltrials.gov/data-api/about-api/study-data-structure)
