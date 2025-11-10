import streamlit as st
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split

st.set_page_config(page_title="🌦 Manila Weather Logger", layout="wide")
st.title("🌦 Manila Weather Logger Dashboard")

# 🔑 Read Neon connection string from Streamlit secrets
conn_str = st.secrets["NEON_CONN"]  # format: 'postgresql+psycopg2://user:pass@host:port/dbname'

# Create SQLAlchemy engine
engine = create_engine(conn_str)

# Fetch all historical weather logs
query = "SELECT * FROM weather_logs ORDER BY timestamp_local DESC;"
df = pd.read_sql(query, engine)

if df.empty:
    st.warning("No data found in weather_logs table.")
else:
    # Show table
    st.subheader("📋 Latest Weather Logs")
    st.dataframe(df, width='stretch')

    # Temperature chart
    st.subheader("🌡 Temperature Trend")
    st.line_chart(df.set_index("timestamp_local")["temperature_c"])

    # Humidity chart
    st.subheader("💧 Humidity Trend")
    st.line_chart(df.set_index("timestamp_local")["humidity_percent"])

    # Condition counts
    st.subheader("☁️ Condition Breakdown")
    st.bar_chart(df["condition"].value_counts())

    # ----------------- Next Hour ML Prediction -----------------
    st.subheader("🔮 Next Hour Temperature Prediction")

    df_sorted = df.sort_values("timestamp_local").copy()

    # Create lag features for last 3 hours
    for lag in range(1, 4):
        df_sorted[f'temp_lag_{lag}'] = df_sorted['temperature_c'].shift(lag)
    
    df_sorted.dropna(inplace=True)  # Drop rows without enough lag

    # Features and target
    X = df_sorted[['temp_lag_1', 'temp_lag_2', 'temp_lag_3']]
    y = df_sorted['temperature_c']

    # Split into train/test (keep time order)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    # Train Linear Regression
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict next hour using last available lags
    latest_lags = X.tail(1)  # keep as DataFrame to preserve column names
    predicted_next_hour = model.predict(latest_lags)[0]
    st.info(f"Predicted next hour temperature: **{predicted_next_hour:.1f} °C**")

    # ----------------- Model Evaluation -----------------
    y_train_pred = model.predict(X_train)
    y_test_pred  = model.predict(X_test)

    rmse_train = np.sqrt(mean_squared_error(y_train, y_train_pred))
    rmse_test  = np.sqrt(mean_squared_error(y_test, y_test_pred))

    eval_df = pd.DataFrame({
        "Dataset": ["Train", "Test"],
        "R²": [model.score(X_train, y_train), model.score(X_test, y_test)],
        "MAE": [mean_absolute_error(y_train, y_train_pred), mean_absolute_error(y_test, y_test_pred)],
        "RMSE": [rmse_train, rmse_test]
    })

    st.subheader("📊 Model Evaluation")
    st.dataframe(eval_df, width='stretch')

    # ----------------- Optional: Predicted vs Actual Plot -----------------
    st.subheader("📈 Predicted vs Actual Temperature (Test Set)")
    test_plot_df = pd.DataFrame({
        "Actual": y_test.values,
        "Predicted": y_test_pred
    }, index=y_test.index)
    st.line_chart(test_plot_df)
