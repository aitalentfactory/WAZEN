
import joblib

model = joblib.load("wazen_text_classifier.pkl")
label_encoder = joblib.load("wazen_label_encoder.pkl")

def classify_transaction(text: str) -> str:
    label = model.predict([text])[0]
    return label_encoder.inverse_transform([label])[0]
