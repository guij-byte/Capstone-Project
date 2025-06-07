import pickle
import numpy as np
import os

class Predictor:
    def __init__(self, model_path='model/model.pkl'):
        if os.path.exists(model_path):
            with open(model_path, "rb") as f:
                self.model = pickle.load(f)
        else:
            raise FileNotFoundError(f"{model_path} not found.")

    def predict_vulnerabilities(self, features: dict):
        features_array = np.array([[features['func_calls'], features['lib_used'], features['lines_of_code']]])

        
        print("input features：", features_array)

        result = self.model.predict(features_array)
        proba = self.model.predict_proba(features_array) if hasattr(self.model, "predict_proba") else None

        print("model predition result：", result)
        if proba is not None:
            print("probability distribution（[No Vulnerability, Vulnerability]）:", proba)

        return {
            "vulnerable": bool(result[0]),
            "probability": float(proba[0][1]) if proba is not None else None
        }
