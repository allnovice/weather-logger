import streamlit as st
import pandas as pd
import psycopg2

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
