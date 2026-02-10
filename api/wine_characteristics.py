from typing import List, Union, Dict, Any

from fastapi import HTTPException

feature_names = ['alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280/od315_of_diluted_wines', 'proline']

Feature = Union[Dict[str, float], List[float]]
Features = Union[List[Feature], Dict[str, float], List[float]]

def dict_to_ordered_list(d: Dict[str, Any]) -> List[float]:
    try:
        return [float(d[name]) for name in feature_names]
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Missing feature: {e.args[0]}")
    except Exception:
        raise HTTPException(status_code=400, detail="Feature values must be numeric")

example_json = {
        "characteristics": {
            "alcohol": 5,
            "malic_acid": 5,
            "ash": 5,
            "alcalinity_of_ash": 5,
            "magnesium": 5,
            "total_phenols": 5,
            "flavanoids": 5,
            "nonflavanoid_phenols": 5,
            "proanthocyanins": 5,
            "color_intensity": 5,
            "hue": 5,
            "od280/od315_of_diluted_wines": 5,
            "proline": 5
        }
}