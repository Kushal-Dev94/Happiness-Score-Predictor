# Happiness Score Predictor

## Overview

The **Happiness Score Predictor** is a machine learning-driven web application that predicts the happiness score of a country based on various socio-economic factors. The model is built using **Linear Regression** and leverages data such as GDP per capita, social support, life expectancy, freedom, generosity, and corruption to provide accurate predictions. The app is built using **Flask** and hosted on **Render**.

## Features

- **Country-based Prediction:** The user can select a country to view its predicted happiness score and compare it with the actual score.
- **Model Analysis:** Visualize the impact of different variables on the happiness score using bar charts and a correlation heatmap.
- **Top Factors Driving Happiness:** A list of the top socio-economic factors that most influence the happiness score.

## How It Works

1. **Data Preprocessing:** 
   - The data from the **World Happiness Report** is cleaned and processed. Missing values are handled, and relevant features like GDP per capita, social support, life expectancy, freedom, generosity, and corruption are extracted.
   
2. **Model Training:** 
   - A **Linear Regression** model is trained using these features to predict happiness scores.
   
3. **Prediction & Visualization:** 
   - After training, the model makes predictions for each country, and the user can view these predictions along with the actual values.
   - The app also visualizes the relationship between variables through a correlation heatmap and variable-wise contributions using bar charts.

## Tech Stack

- **Backend:** Flask
- **Machine Learning:** Scikit-learn (Linear Regression)
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Deployment:** Render
- **Web Design:** HTML, CSS (Tailwind CSS)

## Getting Started

### Prerequisites

Before running the project locally, make sure you have the following installed:

- Python 3.6+
- Pip (Python package manager)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/Happiness-Score-Predictor.git
   cd Happiness-Score-Predictor
