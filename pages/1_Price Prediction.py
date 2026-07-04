import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# load the model
rf = joblib.load(BASE_DIR / "model" / "car_price_model.pkl")

#load the dictionaries
make_freq= joblib.load(BASE_DIR / "model" / "make_freq.pkl")
model_freq = joblib.load(BASE_DIR / "model" / "model_freq.pkl")

#load the dataset
df = pd.read_csv("data/selectForUI_v1.csv")
df['year'] = 2026 - df['car_age']


#load CSS file
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#banner
car = Image.open("assets/pred_banner.png")
st.image(car, width='content')

#inputs
left,right = st.columns([2,1])

with left:

    col1,col2,col3 = st.columns(3)

    with col1:
        assembly = st.selectbox(
            "Assembly Type",df['assembly'].unique().tolist()
        )

    with col2:
        brand = st.selectbox(
            "Brand", df['make'].unique().tolist()
        )
        brand_frequency = make_freq.get(brand, 0)

    with col3:
        available_models = sorted(df[df['make'] == brand]['model'].unique())
        model = st.selectbox(
            "Model", available_models
        )
        model_frequency = model_freq.get(model, 0)

    col1, col2, col3 = st.columns(3)
    with col1:
        available_bodies = sorted(df[(df['make'] == brand) &(df['model'] == model)]['body'].unique())
        body = st.selectbox(
            "Body Type", available_bodies)

    with col2:
        transmission = st.selectbox(
            "Transmission Type", df['transmission'].unique().tolist()
        )
        transmission = 0 if transmission == "Manual" else 1

    with col3:
        fuel = st.selectbox(
            "Fuel Type", df['fuel'].unique().tolist()
        )

    col1, col2, col3 = st.columns(3)
    with col1:
        engine = st.selectbox(
            "Engine Capacity", df['engine'].sort_values().unique().tolist()
        )


    with col2:
        registered_grouped = st.selectbox(
            "Car Registration City", df['registered_grouped'].unique().tolist()
        )

    with col3:
        city = st.selectbox(
            "Buying/Selling City ", df['city_grouped'].unique().tolist()
        )

    available_years = sorted(df[(df['make'] == brand) &(df['model'] == model) &(df['body'] == body)]['year'].unique(),
        reverse=True)
    year = st.selectbox(
        "Model Year",available_years)
    year = 2026 - year

    mileage = np.log1p(st.number_input(
        "Mileage",
        min_value=100,
    ))


    input_data = pd.DataFrame({'assembly':[assembly],
                               'body':[body],
                               'engine':[engine],
                               'transmission':[transmission],
                               'fuel':[fuel],
                               'car_age':[year],
                               'city_grouped':[city],
                               'registered_grouped':[registered_grouped],
                               'log_mileage':[mileage],
                               'make_freq':[brand_frequency],
                               'model_freq':[model_frequency]})
    prediction = rf.predict(input_data)

    btn = st.button("Predict Price")
    log_price = prediction[0]
    actual_price =0

    if btn:

        actual_price = np.expm1(log_price)

with right:

    money = Image.open("assets/moneyy.png")

    st.markdown(f"""
    <div class="prediction-box">
    <h4 style = text-align:left;>🏆 Prediction Result</h4>
    <p>Your predicted car price</p>

    <div class="price-text">
    <h2>PKR {actual_price:,.0f}</h2>
    </div>
    <div class="price-text">
    </div>
    
    <h5>{brand} {model} {2026 - year}</h5>
    </div>
    """, unsafe_allow_html=True)

    st.image(money,width=1000)
