import pandas as pd
import xgboost as xgb
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def train_and_save_model():
   
    data = pd.DataFrame({
        'func_calls': [3, 7, 5, 2, 9],
        'lib_used': [1, 0, 1, 0, 1],
        'lines_of_code': [20, 35, 30, 12, 50],
        'vulnerable': [0, 1, 1, 0, 1]
    })
    data['vulnerable'] = ((data['func_calls'] > 7) & (data['lines_of_code'] > 40)).astype(int)
    X = data.drop('vulnerable', axis=1)
    y = data['vulnerable']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = xgb.XGBClassifier()
    model.fit(X_train, y_train)

    print(classification_report(y_test, model.predict(X_test)))

 
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)
    print(" model is successfully saved as model.pkl")

if __name__ == "__main__":
    train_and_save_model()
