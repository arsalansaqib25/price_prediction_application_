import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Car Dashboard",
    page_icon="🚗",
    layout="wide"
)

# LOAD CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



# HERO SECTION
banner = Image.open("assets/banner_car.png")
st.image(banner, width='content')


st.title('Welcome')
st.markdown("""
   <div class="welcome_card">
       <p>Welcome to the Car Price Prediction & Analytics Dashboard — an intelligent platform designed to analyze vehicle market trends and estimate car prices using Machine Learning techniques.
       This dashboard helps users explore car data through interactive visualizations, statistical insights, and predictive analytics. Users can compare prices across different brands, fuel types, transmission systems, model years, and other important features that influence car valuation.</p>
<h3>Main Features</h3>
<h4>Car Price Prediction</h4>
Predict estimated car prices based on user inputs - Machine Learning powered prediction system - Fast and accurate price estimation
<h4>Interactive Analytics</h4>
Visualize price distributions and market trends - Compare prices between different car brands and categories - Explore relationships between mileage, engine size, year, and price
<h4>User-Friendly Dashboard</h4>
Clean and responsive Streamlit interface - Easy navigation with sidebar menu - Real-time interaction and analysis


<p>This project demonstrates the practical use of Data Science, Machine Learning, and Data Visualization for solving real-world automobile pricing problems.</p>
   </div>
   """, unsafe_allow_html=True)

# METRICS
c1, c2, c3, c4= st.columns(4)

with c1:
    st.markdown("""
    <div class="metric-card">
        <h1>🎯</h1>
        <h2>94.99%</h2>
        <p>R² Score</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-card">
        <h1>📉</h1>
        <h2>11.28%</h2>
        <p>MAPE</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-card">
        <h1>💰</h1>
        <h2>331K PKR</h2>
        <p>MAE</p>
    </div>
    """, unsafe_allow_html=True)
with c4:
    st.markdown("""
    <div class="metric-card">
        <h1>💵</h1>
        <h2>893K PKR</h2>
        <p>RMSE</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="footer">
© 2026 Car Price Prediction Dashboard
</div>
""", unsafe_allow_html=True)