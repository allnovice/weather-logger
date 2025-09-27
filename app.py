import streamlit as st
import pandas as pd
import psycopg2
from sklearn.linear_model import LinearRegression
import numpy as np

st.set_page_config(page_title="🌦 Manila Weather Logger", layout="wide")
st.title("🌦 Manila Weather Logger Dashboard")

# 🔑 Read Neon connection string from Streamlit secrets
conn_str = st.secrets["NEON_CONN"]

# Connect to Neon
conn = psycopg2.connect(conn_str)

# Fetch latest 50 rows
query = "SELECT * FROM weather_logs ORDER BY timestamp_local DESC LIMIT 50;"
df = pd.read_sql(query, conn)

if df.empty:
    st.warning("No data found in weather_logs table.")
else:
    # Show table
    st.subheader("📋 Latest Weather Logs")
    st.dataframe(df, use_container_width=True)

    # Temperature chart
    st.subheader("🌡 Temperature Trend")
    st.line_chart(df.set_index("timestamp_local")["temperature_c"])

    # Humidity chart
    st.subheader("💧 Humidity Trend")
    st.line_chart(df.set_index("timestamp_local")["humidity_percent"])

    # Condition counts
    st.subheader("☁️ Condition Breakdown")
    st.bar_chart(df["condition"].value_counts())

    # ----------------- Simple ML Prediction -----------------
    st.subheader("🔮 Predicted Temperature for Tomorrow")

    # Prepare data for regression
    df_sorted = df.sort_values("timestamp_local")
    df_sorted['day_index'] = np.arange(len(df_sorted))
    
    X = df_sorted[['day_index']]  # Features (time)
    y = df_sorted['temperature_c']  # Target

    # Train linear regression
    model = LinearRegression()
    model.fit(X, y)

    # Predict for next day
    next_day_index = np.array([[len(df_sorted)]])
    predicted_temp = model.predict(next_day_index)[0]

    st.info(f"Predicted temperature for tomorrow: **{predicted_temp:.1f} °C**")
