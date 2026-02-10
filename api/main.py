import pickle

from fastapi import FastAPI, Body
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

from pydantic import BaseModel
import wine_characteristics as wine

app = FastAPI()

model = None

class Request(BaseModel):
    characteristics: wine.Features

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Wine Clasificator",
        version="1.0.0",
        description="wine clasificator using AI model",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

def load_model():
    global model
    if not model is None:
        return model
    model = pickle.load(open('../model/model.pkl', 'rb'))
    return model

@app.get("/doc", include_in_schema=False)
def swagger_ui():
    app.openapi = custom_openapi
    return get_swagger_ui_html(
        title="Wine Clafificator",
        openapi_url="/openapi.json"
    )

@app.post("/predict")
def predict_endpoint(req: Request = Body(..., example=wine.example_json)):
    wine_features = req.characteristics
    data = wine.dict_to_ordered_list(wine_features)
    model = load_model()
    category = model.predict([data])
    return {"category": f'{category}'}
    # return {"category": f'{data}'}
