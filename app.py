from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load dataset (sample CSV expected)
try:
    events = pd.read_csv("customer_features_sample.csv")
except:
    events = pd.DataFrame(columns=["visitorid", "itemid"])

# Simple recommendation function
def recommend_items(user_id):
    user_events = events[events["visitorid"] == user_id]
    if user_events.empty:
        return ["No history found"]
    last_item = user_events.iloc[-1]["itemid"]
    return [f"Recommended item based on last purchase: {last_item}"]

@app.route("/", methods=["GET", "POST"])
def home():
    recs = []
    if request.method == "POST":
        try:
            user_id = int(request.form["userid"])
            recs = recommend_items(user_id)
        except:
            recs = ["Invalid User ID"]
    return render_template("index.html", recs=recs)

if __name__ == "__main__":
    app.run(debug=True)
