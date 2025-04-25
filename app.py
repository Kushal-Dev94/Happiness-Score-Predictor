from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load model and processed data
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

data = pd.read_csv("data/processed_data.csv")
countries = sorted(data["country"].unique())
top_factors_df = pd.read_csv("data/top_factors.csv", index_col=0)
max_factor_value = top_factors_df.iloc[0, 0]
top_factors = list(top_factors_df.iterrows())

@app.route("/", methods=["GET", "POST"])
def index():
    selected_country = None
    result = None

    if request.method == "POST":
        selected_country = request.form["country"]
        country_data = data[data["country"] == selected_country].iloc[0]
        actual_score = country_data["score"]
        predicted_score = country_data["predicted_score"]
        error = ((predicted_score - actual_score)/actual_score) * 100

        result = {
            "country": selected_country,
            "actual": round(actual_score, 3),
            "predicted": round(predicted_score, 3),
            "error": round(error, 3),
            "gdp": country_data["gdp_per_capita"],
            "support": country_data["social_support"],
            "health": country_data["healthy_life_expectancy"],
            "freedom": country_data["freedom"],
            "generosity": country_data["generosity"],
            "corruption": country_data["corruption"]
        }

    return render_template(
        "index.html",
        countries=countries,
        result=result,
        selected=selected_country,
        top_factors=top_factors,
        max_value=max_factor_value
    )

if __name__ == "__main__":
    app.run(debug=True)
