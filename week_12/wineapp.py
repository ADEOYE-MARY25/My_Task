from fastapi import FastAPI
import numpy as np
import joblib
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV, cross_val_score
from sklearn.metrics import classification_report
from random import randint
from pydantic import BaseModel

app= FastAPI()

scaler =joblib.load('scaler.pkl')
model = joblib.load('best_model.pkl')

class Data(BaseModel):
    fixed_acidity: float
    valatile_acidity: float
    citric_acid:float
    residual_sugar:float
    chlorides:float
    free_sulfur_dioxide:float
    total_sulfur_dioxide:float
    density:float
    sulphates:float
    alcohol:float

@app.get("/")
def home():
    return {"message" "welcome to wine quality predictor"}

@app.post("/predict")
def get_wine_quality(input: Data):
    features = np.array([[
        input.fixed_acidity,
        input.valatile_acidity,
        input.citric_acid,
        input.residual_sugar,
        input.chlorides,
        input.free_sulfur_dioxide,
        input.total_sulfur_dioxide,
        input.density,
        input.sulphates,
        input.alcohol
    ]])

    scaled_feature = scaler.transform(features)
    prediction= model.predict(scaled_feature)

    return {"predicted wine quality":str(prediction[0])}

