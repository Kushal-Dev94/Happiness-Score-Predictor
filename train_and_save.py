import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
import os
import seaborn as sns
import matplotlib.pyplot as plt

# Load and preprocess
df = pd.read_csv("data/report_2018-2019.csv")
df.columns = [
    "overall_rank", "country", "year", "score", "gdp_per_capita",
    "social_support", "healthy_life_expectancy", "freedom",
    "generosity", "corruption"
]
df.dropna(inplace=True)

features = ["gdp_per_capita", "social_support", "healthy_life_expectancy", "freedom", "generosity", "corruption"]
target = "score"

X = df[features]
y = df[target]

# Train
model = LinearRegression()
model.fit(X, y)

# Save model
os.makedirs("model", exist_ok=True)
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

# Add predictions to data
df["predicted_score"] = model.predict(X)
df.to_csv("data/processed_data.csv", index=False)

# Correlation heatmap
corr = df[features + [target]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("static/heatmap.png")
plt.close()

# Coefficients chart
coefs = pd.Series(model.coef_, index=features)
coefs.sort_values().plot(kind="barh", color="skyblue")
plt.title("Impact of Variables on Happiness Score")
plt.xlabel("Regression Coefficient")
plt.tight_layout()
plt.savefig("static/coefficients.png")
plt.close()

# Top 10 factors (here all features, but sorted)
top_factors = coefs.abs().sort_values(ascending=False).head(10)
top_factors.to_csv("data/top_factors.csv")
