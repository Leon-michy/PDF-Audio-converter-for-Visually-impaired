import joblib

model = joblib.load("models/read_classifier.pkl")

tests = [
    "Page 25",
    "Figure 7",
    "Machine learning improves healthcare.",
    "Conclusion",
    "www.openai.com"
]

for text in tests:
    prediction = model.predict([text])[0]
    print(f"{text} --> {prediction}")