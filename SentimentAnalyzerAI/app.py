from flask import Flask, render_template, request

app = Flask(__name__)

def analyze_sentiment(text):
    text = text.lower()
    if "good" in text or "happy" in text:
        return "Positive 😊"
    elif "bad" in text or "sad" in text:
        return "Negative 😔"
    else:
        return "Neutral 😐"

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        text = request.form["text"]
        result = analyze_sentiment(text)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)