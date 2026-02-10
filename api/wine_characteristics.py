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
            "alcohol": 13.88,
            "malic_acid": 5.04,
            "ash": 2.23,
            "alcalinity_of_ash": 20,
            "magnesium": 80,
            "total_phenols": .98,
            "flavanoids": .34,
            "nonflavanoid_phenols": .4,
            "proanthocyanins": .68,
            "color_intensity": 4.9,
            "hue": .58,
            "od280/od315_of_diluted_wines": 1.33,
            "proline": 415
        }
}