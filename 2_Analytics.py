import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

#load the CSS file
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#load the dataset
df = pd.read_csv("data/selectForUI_v1.csv")
importance_df =pd.read_csv("data/importance_df.csv")
results = pd.read_csv("data/result_df.csv")

#banner
analytics = Image.open("assets/anal_banner.png")
st.image(analytics, width='content')

# METRICS CARD
st.subheader("📊 Dataset Overview")
c1, c2, c3 ,c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="metric-card">
        <h1>🚘</h1>
        <h2> {len(df)} </h2>
        <p>Cars Analyzed</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric-card">
       <h1>💰</h1>
        <h2>{round(df['price'].mean()/1000000,1)}M PKR</h2>
        <p>Average Price</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-card">
        <h1>🛣️</h1>
        <h2>{round(df['mileage'].mean()):,.0f}</h2>
        <p>Average Mileage</p>
    </div>
    """, unsafe_allow_html=True)
with c4:
    st.markdown(f"""
    <div class="metric-card">
        <h1>🚗</h1>
        <h2>{df['make'].nunique()}</h2>
        <p>Total Brands</p>
    </div>
    """, unsafe_allow_html=True)

#market insights
st.header('Market Insights')
#price distribution chart
st.subheader("📊 Price Distribution")
fig = px.histogram(df,x='price',nbins=50,title='Price Distribution')
fig.update_traces(marker_color='orange')
fig.update_layout(template="plotly_dark",xaxis_title="Price",height=600)
st.plotly_chart(fig, use_container_width=True)

#Brand market share chat
st.subheader("🚗 Top Brand Market Share")
brand_counts = df['make'].value_counts().head(15)
market_share = (brand_counts / len(df) * 100).round(1)
fig = px.bar( x=brand_counts.index, y=market_share.values,text=[f"{x}%" for x in market_share],title="Top 15 Brands Market Share (%)")
fig.update_traces(textposition="outside",marker_color='orange')
fig.update_layout(template="plotly_dark",xaxis_title="Brand",yaxis_title="Market Share (%)",height=600,xaxis_tickangle=-45)
st.plotly_chart(fig, use_container_width=True)


#market depreciation curve
st.subheader("📉 Market Depreciation Curve")
depreciation = (df.groupby('car_age')['price'].median().reset_index())
fig = px.line(depreciation,x='car_age',y='price',markers=True,title='Vehicle Depreciation Curve')
st.plotly_chart(fig, use_container_width=True)

#EDA charts
st.header('Vehicle Insights')
#engine x age heatmap
df['engine_bin'] = pd.cut(df['engine'],bins=[0,1000,1500,2000,2500,3000,4000,7000],
                          labels=['<1000','1000-1500','1500-2000','2000-2500','2500-3000','3000-4000','4000+'])
st.subheader("🔥 Engine × Age Heatmap")
pivot = pd.pivot_table(df,values='price',index='engine_bin',columns='car_age',aggfunc='median')
fig = px.imshow(pivot,text_auto=True,aspect='auto',title='Median Price Heatmap',color_continuous_scale="Turbo",
                labels={"x": "Car Age","y": "Engine","color": "Price"})
st.plotly_chart(fig, use_container_width=True)

#mileage vs price
st.subheader("🛣️ Mileage vs Price")
sample_df = df.sample(min(5000,len(df)),random_state=42)
fig = px.scatter(sample_df,x='mileage',y='price',color='fuel',opacity=0.6,title='Mileage vs Price')
st.plotly_chart(fig, use_container_width=True)

#model evaluation chart
st.header('Model Performance')
#feature importance
st.subheader("⭐ Feature Importance")
top_features= (importance_df.sort_values('Importance',ascending=False).head(10))
importance = (top_features['Importance'] * 100).round(1)
fig = px.bar( x=top_features['Feature'], y=importance,text=[f"{x}%" for x in importance],title="Top 10 Important Features (%)")
fig.update_traces(textposition="outside",marker_color='orange')
fig.update_layout(template="plotly_dark",xaxis_title="Features",yaxis_title="Importance (%)",height=600,xaxis_tickangle=-45)
st.plotly_chart(fig, use_container_width=True)


#model comparison
st.subheader("⚖️ Model Comparison")

#actual vs predicted
st.subheader("🎯 Actual vs Predicted")
fig = px.scatter(results,x='Actual',y='Predicted',opacity=0.5,title='Actual vs Predicted Prices')
fig.add_shape(type='line',x0=results['Actual'].min(),y0=results['Actual'].min(),x1=results['Actual'].max(),y1=results['Actual'].max(),line=dict(color="red"))
st.plotly_chart(fig, use_container_width=True)

#resediual distribution
st.subheader("📈 Residual Distribution")
residuals = results['Actual'] - results['Predicted']
fig = px.histogram(residuals,nbins=50,title='Residual Distribution')
fig.update_traces(marker_color='orange')
st.plotly_chart(fig, use_container_width=True)


#footer
st.markdown("""
<div class="footer">
© 2026 Car Price Prediction Dashboard
</div>
""", unsafe_allow_html=True)