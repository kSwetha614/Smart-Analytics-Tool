import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Smart Analytics Tool", layout="wide")

st.title("📊 Smart Analytics Tool")

# Upload CSV
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:

    # Read Dataset
    df = pd.read_csv(uploaded_file)

    # Dataset Preview
    st.header("📌 Dataset Preview")
    st.dataframe(df.head())

    # Dataset Shape
    st.write("Rows and Columns:", df.shape)

    # Missing Values
    st.header("🧹 Missing Value Analysis")
    st.write(df.isnull().sum())

    # Statistical Summary
    st.header("📈 Statistical Summary")
    st.write(df.describe())

    # Column Selection
    numeric_columns = df.select_dtypes(include=['number']).columns

    # Visualization 1
    st.header("📊 Histogram")

    hist_col = st.selectbox("Select Column for Histogram", numeric_columns)

    fig = px.histogram(df, x=hist_col)

    st.plotly_chart(fig)

    # Visualization 2
    st.header("📉 Scatter Plot")

    x_col = st.selectbox("Select X-axis", numeric_columns)

    y_col = st.selectbox("Select Y-axis", numeric_columns)

    fig = px.scatter(df, x=x_col, y=y_col)

    st.plotly_chart(fig)

    # Visualization 3
    st.header("📋 Bar Chart")

    bar_col = st.selectbox("Select Column for Bar Chart", numeric_columns)

    bar_data = df[bar_col].value_counts().reset_index()

    bar_data.columns = ["Value", "Count"]

    fig = px.bar(bar_data, x="Value", y="Count")

    st.plotly_chart(fig)

else:
    st.info("Please upload a CSV file.")
