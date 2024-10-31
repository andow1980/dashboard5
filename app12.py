import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df = px.data.tips()

# --- Page 1 ---
st.header("Page 1: Time-Based Analysis")
tab1, tab2 = st.tabs(['Histogram', 'Box Plot'])

time_filter = st.sidebar.radio('Select Time', df['time'].unique())
filtered_df = df[df['time'] == time_filter]

with tab1:
    st.subheader("Histogram of Total Bill")
    st.plotly_chart(px.histogram(filtered_df, x="total_bill", title="Total Bill Distribution"))

with tab2:
    st.subheader("Box Plot of Total Bill")
    st.plotly_chart(px.box(filtered_df, x="total_bill", title="Total Bill Distribution"))

# --- Page 2 ---
st.header("Page 2: Sex-Based Analysis")
col1, col2 = st.columns(2)

sex_filter = st.sidebar.selectbox('Select Sex', df['sex'].unique())
filtered_df = df[df['sex'] == sex_filter]

with col1:
    st.subheader("Histogram of Total Bill")
    st.plotly_chart(px.histogram(filtered_df, x="total_bill", title="Total Bill Distribution"))

with col2:
    st.subheader("Scatter Plot of Total Bill vs. Tip")
    st.plotly_chart(px.scatter(filtered_df, x="total_bill", y="tip", title="Total Bill vs. Tip"))

# --- Page 3 ---
st.header("Page 3: Smoker-Based Analysis")
tab1, tab2 = st.tabs(['Violin Plot', 'Scatter Plot'])

smoker_filter = st.sidebar.radio('Select Smoker', df['smoker'].unique())
filtered_df = df[df['smoker'] == smoker_filter]

with tab1:
    st.subheader("Violin Plot of Total Bill")
    st.plotly_chart(px.violin(filtered_df, x="smoker", y="total_bill", title="Total Bill Distribution"))

with tab2:
    st.subheader("Scatter Plot of Total Bill vs. Tip")
    st.plotly_chart(px.scatter(filtered_df, x="total_bill", y="tip", title="Total Bill vs. Tip"))
