import streamlit as st
from PIL import Image


#load CSS file
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#banner
about = Image.open("assets/about_banner.png")
st.image(about, width='content')


#about the project
st.markdown("""
<div class="custom-card">
<p>
This project is an end-to-end Machine Learning application developed to predict used car prices in Pakistan based on vehicle specifications and market characteristics.

The system combines comprehensive data preprocessing, feature engineering, exploratory data analysis (EDA), machine learning model comparison, and an interactive Streamlit dashboard to provide accurate price predictions and valuable market insights.

</p>
</div>
""", unsafe_allow_html=True)

#about the dataset
st.markdown("""
<div class="custom-card">
<h2>📊 Dataset Overview</h2>
<h3>Dataset Features</h3>
<p>The dataset contains information about used vehicles listed in the Pakistani automobile market.</p>
<h4>Original Features</h4>
<table><tr>
<th>City</th><th>Assembly</th><th>Body</th><th>Make</th>
<th>Model</th><th>Year<th><th>Engine</th><th>Transmission</th><th>Fuel</th>
<th>Color</th><th>Registered</th><th>Mileage</th><th>Price</th>
</tr></table>

<h4>Engineered Features</h4>
<table><tr>
<th>Car Age</th><th>Make Frequency</th><th>Model Frequency</th><th>Log Mileage</th><th>Log Price</th>
</tr></table>
<p>Feature engineering significantly improved model performance by extracting meaningful patterns from raw data.</p>
</div>
""", unsafe_allow_html=True)

#Comparison tabe/ model selection
st.markdown("""
<div class="custom-card">

<h2>🏆 Model Performance Comparison</h2>
<table><tr><th>Model</th><th>R² Score</th></tr>
  <tr><td>Random Forest</td><td>94.9%</td></tr>
  <tr><td>Random Forest (Tuned)</td><td>94.6%</td></tr>
  <tr><td>XGBoost</td><td>94.7%</td></tr>
  <tr><td>Catboost</td><td>93.4%</td></tr>
  <tr><td>Linear Regression</td><td>77.1%</td></tr>
  <tr><td>SVR</td><td>62.1%</td></tr>
</table>

<h2>Selected Model</h2>
<p>
Random Forest Regressor was selected as the final deployment model based on its superior performance and generalization ability.
</p>
<h2>Key Insights</h2>
<h3>Major Findings</h3>
<p>- Automatic transmission vehicles tend to command significantly higher prices.</p>
<p>- Car age is one of the strongest predictors of vehicle value.</p>
<p>- Engine capacity strongly influences market price.</p>
<p>- Imported SUVs and luxury vehicles contribute to the largest prediction errors.</p>
<p>- Tree-based ensemble methods outperform traditional regression techniques for this dataset.</p>
</div>
""", unsafe_allow_html=True)

#Technologies used
st.markdown("""
<div class="custom-card">
<h2>🔧 Technologies Used</h2>
<h3>Programming</h3>
<ul><li>Python</li></ul>

<h3>Data Analysis</h3>
<ul><li>NumPy</li><li>Pandas</li></ul>

<h3>Visualization</h3>
<ul><li>Matplotlib</li><li>Seaborn</li><li>Plotly</li></ul>

<h3>Machine Learning</h3><ul><li>Scikit-Learn</li><li>XGBoost</li><li>CatBoost</li></ul>

<h3>Deployment</h3><ul><li>Streamlit</li></ul>
</div>
""", unsafe_allow_html=True)

#futur improvement
st.markdown("""
<div class="custom-card">
<h2>🚀 Future Improvements</h2>
Potential enhancements include:

- Vehicle condition information
- Accident history
- Ownership records
- Variant-level details
- Real-time market data integration
- Deep Learning approaches
- API-based deployment
</div>
""", unsafe_allow_html=True)


#footer
st.markdown("---")
st.markdown("""
### Project Supervisor
**Sir Nizam Ahmad**
### Developed By

**Arsalan Saqib**

**Muhammad Anas**

BS Computer Science
""")
st.markdown("""
<div class="footer">
© 2026 Car Price Prediction Dashboard
</div>
""", unsafe_allow_html=True)