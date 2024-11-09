# train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Load and preprocess your dataset
data = pd.read_csv('/Users/vanshtomar/Downloads/data.csv')
symptom_columns = ['symptoms1', 'symptoms2', 'symptoms3', 'symptoms4', 'symptoms5']
for column in symptom_columns:
    data[column] = data[column].fillna("None")

# One-hot encoding for symptoms
data = pd.get_dummies(data, columns=symptom_columns)
label_encoder = LabelEncoder()
data['Dangerous'] = label_encoder.fit_transform(data['Dangerous'])

X = data.drop(columns=['AnimalName', 'Dangerous'])
y = data['Dangerous']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'model.pkl')
