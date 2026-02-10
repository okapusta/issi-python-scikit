issi-python-scikit
=====
A simple web service build for wine classification using Scikit learn wine dataset

## Prerequisites

- Python
- [uv](https://github.com/astral-sh/uv)

Then sync deps...

```
uv sync
```

## Model

### Training

```
uv run model/train.py
```

### Usage

See example.py for details

```
uv run example.py
```

## API

Run from the main directory:

```
uv run fastapi dev api/main.py
```

Example prediction:

```
curl -X POST localhost:8000/predict -H 'Content-Type: application/json' -d '{
    "characteristics": {
        "alcohol": 12.37,
        "malic_acid": 0.94,
        "ash": 1.36,
        "alcalinity_of_ash": 10.6,
        "magnesium": 88,
        "total_phenols": 1.98,
        "flavanoids": 0.57,
        "nonflavanoid_phenols": 0.28,
        "proanthocyanins": 0.42,
        "color_intensity": 1.95,
        "hue": 1.05,
        "od280/od315_of_diluted_wines": 1.82,
        "proline": 520
    }
}'

```
