import streamlit as st
import pandas as pd
import psycopg2

st.title("🌦 Manila Weather Logger")

# Neon DB connection
conn = psycopg2.connect(os.environ["NEON_CONN"])

df = pd.read_sql("SELECT * FROM weather_logs ORDER BY timestamp_local DESC LIMIT 20;", conn)
st.write("### Latest Weather Logs", df)

st.line_chart(df.set_index("timestamp_local")["temperature_c"])
