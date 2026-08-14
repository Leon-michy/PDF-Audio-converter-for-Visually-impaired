import joblib


class TextClassifier:

    def __init__(self):
        self.model = joblib.load(
            "models/read_classifier.pkl"
        )

    def analyze(self, text):

        lines = text.split("\n")

        results = []

        useful_lines = []

        for line in lines:

            line = line.strip()

            if line == "":
                continue

            prediction = self.model.predict([line])[0]

            results.append({
                "text": line,
                "prediction": prediction
            })

            if prediction == "Read":
                useful_lines.append(line)

        return {
            "filtered_text": "\n".join(useful_lines),
            "results": results,
            "total": len(results),
            "read": len(useful_lines),
            "ignored": len(results) - len(useful_lines)
        }