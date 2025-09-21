import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import json
import warnings

warnings.filterwarnings("ignore")

# -------------------------------
# File Loader
# -------------------------------
def import_data():
    st.header("📂 Upload Your Fitness File")
    uploaded_file = st.file_uploader(
        "Select a data file (CSV or JSON)", type=["csv", "json"], accept_multiple_files=False
    )

    if uploaded_file:
        try:
            if uploaded_file.name.endswith(".csv"):
                dataset = pd.read_csv(uploaded_file)
            else:
                dataset = pd.DataFrame(json.load(uploaded_file))
            st.success(f"✅ File '{uploaded_file.name}' loaded successfully ({len(dataset)} records)")
            return dataset
        except Exception as e:
            st.error(f"❌ Failed to load file: {e}")
            return pd.DataFrame()
    return pd.DataFrame()


# -------------------------------
# Data Cleaning
# -------------------------------
def preprocess_data(data: pd.DataFrame):
    if data.empty:
        return data

    # Normalize column names
    data = data.rename(columns={"datetime": "timestamp", "sleep_duration": "duration_minutes"})
    data.columns = data.columns.str.lower()

    # Ensure timestamp is valid
    data["timestamp"] = pd.to_datetime(data["timestamp"], errors="coerce")
    data = data.dropna(subset=["timestamp"])

    # Convert metrics to numeric and clean
    for col in ["heart_rate", "step_count", "duration_minutes"]:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors="coerce").fillna(0).clip(lower=0)

    return data


# -------------------------------
# Resampling & Filling
# -------------------------------
def align_data(data, interval="1H", fill_method="interpolate"):
    if "timestamp" not in data:
        return data

    data = data.set_index("timestamp").resample(interval).mean()

    if fill_method == "interpolate":
        data = data.interpolate().bfill().ffill()
    elif fill_method == "forward_fill":
        data = data.ffill()
    elif fill_method == "backward_fill":
        data = data.bfill()
    elif fill_method == "zero":
        data = data.fillna(0)
    elif fill_method == "drop":
        data = data.dropna()

    return data.reset_index()


# -------------------------------
# Visualization
# -------------------------------
def show_visuals(data):
    if data.empty:
        st.warning("⚠ No data available for visualization.")
        return

    st.subheader("🔎 Quick Data Preview")
    st.dataframe(data.head(15))

    metrics = [c for c in data.columns if c != "timestamp"]
    if metrics:
        metric_choice = st.selectbox("Select a metric to plot", metrics)
        fig = go.Figure(go.Scatter(x=data["timestamp"], y=data[metric_choice], mode="lines+markers"))
        fig.update_layout(
            title=f"{metric_choice.capitalize()} Over Time",
            xaxis_title="Time",
            yaxis_title=metric_choice.capitalize(),
        )
        st.plotly_chart(fig, use_container_width=True)


# -------------------------------
# Main Workflow
# -------------------------------
def fitness_pipeline():
    st.set_page_config(page_title="Fitness Data Pipeline", page_icon="💪", layout="wide")
    st.title("💪 Fitness Data Cleaning & Visualization Tool")

    # Sidebar Options
    freq_options = {"1 min": "1T", "5 min": "5T", "15 min": "15T", "30 min": "30T", "1 hour": "1H"}
    freq_choice = st.sidebar.selectbox("⏱ Resampling Interval", list(freq_options.keys()), index=4)
    fill_choice = st.sidebar.selectbox(
        "🛠 Fill Missing Values",
        ["interpolate", "forward_fill", "backward_fill", "zero", "drop"],
        index=0,
    )

    # Data Pipeline Execution
    raw_data = import_data()
    if not raw_data.empty:
        clean_data = preprocess_data(raw_data)
        aligned_data = align_data(clean_data, interval=freq_options[freq_choice], fill_method=fill_choice)
        st.success("✅ Data pipeline executed successfully")
        show_visuals(aligned_data)


if __name__ == "__main__":
    fitness_pipeline()
