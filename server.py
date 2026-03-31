from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return "Emotion Detector is running"

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')

    # Handle empty input
    if not text_to_analyze:
        return "Invalid input! Please try again."

    result = emotion_detector(text_to_analyze)

    # Handle API error
    if result['dominant_emotion'] is None:
        return "Invalid input! Please try again."

    return str(result)

if __name__ == "__main__":
    app.run(debug=True)