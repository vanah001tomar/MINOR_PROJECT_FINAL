# recommend.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the pre-trained model (make sure to train and save it in a separate script)
model = joblib.load("model.pkl")

def get_recommendation(symptoms):
    """
    Takes a dictionary of symptoms and returns a health recommendation.
    """
    # Create a DataFrame from the symptoms dictionary
    test_df = pd.DataFrame([symptoms])
    
    # Apply one-hot encoding to match the model's feature format
    test_df = pd.get_dummies(test_df).reindex(columns=model.feature_names_in_, fill_value=0)
    
    # Predict with the trained model
    prediction = model.predict(test_df)[0]
    return "Dangerous" if prediction == 1 else "Not Dangerous"
