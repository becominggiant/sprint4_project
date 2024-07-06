import streamlit as st
import pandas as pd
import plotly.express as px

# Load your data
df = pd.read_csv("C:/Users/CRcha/OneDrive/Desktop/coding/sprint4project/sprint4_project/vehicles_us.csv")

# Title of the Streamlit app
st.title("Car Listings Analysis")

# Streamlit header
st.header("Explore the Dataset")

# Checkbox to show/hide Price Distribution Histogram
if st.checkbox('Show Price Distribution Histogram'):
    st.subheader('Price Distribution')
    fig = px.histogram(df, x='price', title='Price Distribution')
    st.plotly_chart(fig)

# Checkbox to show/hide Model Year Distribution Histogram
if st.checkbox('Show Model Year Distribution Histogram'):
    st.subheader('Model Year Distribution')
    fig = px.histogram(df, x='model_year', title='Model Year Distribution')
    st.plotly_chart(fig)

# Checkbox to show/hide Odometer Readings Distribution Histogram
if st.checkbox('Show Odometer Readings Distribution Histogram'):
    st.subheader('Odometer Readings Distribution')
    fig = px.histogram(df, x='odometer', title='Odometer Readings Distribution')
    st.plotly_chart(fig)

# Checkbox to show/hide Days Listed Distribution Histogram
if st.checkbox('Show Days Listed Distribution Histogram'):
    st.subheader('Days Listed Distribution')
    fig = px.histogram(df, x='days_listed', title='Days Listed Distribution')
    st.plotly_chart(fig)

# Checkbox to show/hide Price vs. Odometer Scatter Plot
if st.checkbox('Show Price vs. Odometer Scatter Plot'):
    st.subheader('Price vs. Odometer (Mileage)')
    fig = px.scatter(df, x='odometer', y='price', title='Price vs. Odometer (Mileage)')
    st.plotly_chart(fig)

# Checkbox to show/hide Price vs. Model Year Scatter Plot
if st.checkbox('Show Price vs. Model Year Scatter Plot'):
    st.subheader('Price vs. Model Year')
    fig = px.scatter(df, x='model_year', y='price', title='Price vs. Model Year')
    st.plotly_chart(fig)

# Checkbox to show/hide Price vs. Cylinders Scatter Plot
if st.checkbox('Show Price vs. Cylinders Scatter Plot'):
    st.subheader('Price vs. Cylinders')
    fig = px.scatter(df, x='cylinders', y='price', title='Price vs. Cylinders')
    st.plotly_chart(fig)

# Checkbox to show/hide Number of Listings by Condition Bar Plot
if st.checkbox('Show Number of Listings by Condition'):
    st.subheader('Number of Listings by Condition')
    fig = px.bar(df, x='condition', title='Number of Listings by Condition')
    st.plotly_chart(fig)

# Checkbox to show/hide Number of Listings by Fuel Type Bar Plot
if st.checkbox('Show Number of Listings by Fuel Type'):
    st.subheader('Number of Listings by Fuel Type')
    fig = px.bar(df, x='fuel', title='Number of Listings by Fuel Type')
    st.plotly_chart(fig)

# Checkbox to show/hide Number of Listings by Transmission Type Bar Plot
if st.checkbox('Show Number of Listings by Transmission Type'):
    st.subheader('Number of Listings by Transmission Type')
    fig = px.bar(df, x='transmission', title='Number of Listings by Transmission Type')
    st.plotly_chart(fig)

# Checkbox to show/hide Price by Condition Box Plot
if st.checkbox('Show Price by Condition Box Plot'):
    st.subheader('Price by Condition')
    fig = px.box(df, x='condition', y='price', title='Price by Condition')
    st.plotly_chart(fig)

# Checkbox to show/hide Price by Fuel Type Box Plot
if st.checkbox('Show Price by Fuel Type Box Plot'):
    st.subheader('Price by Fuel Type')
    fig = px.box(df, x='fuel', y='price', title='Price by Fuel Type')
    st.plotly_chart(fig)

# Checkbox to show/hide Price by Transmission Type Box Plot
if st.checkbox('Show Price by Transmission Type Box Plot'):
    st.subheader('Price by Transmission Type')
    fig = px.box(df, x='transmission', y='price', title='Price by Transmission Type')
    st.plotly_chart(fig)

# Checkbox to show/hide Correlation Matrix Heatmap
if st.checkbox('Show Correlation Matrix Heatmap'):
    st.subheader('Correlation Matrix Heatmap')
    correlation_matrix = df[['price', 'model_year', 'odometer', 'days_listed', 'cylinders']].corr()
    fig = px.imshow(correlation_matrix, title='Correlation Matrix Heatmap')
    st.plotly_chart(fig)

# Checkbox to show/hide Scatter Matrix
if st.checkbox('Show Scatter Matrix'):
    st.subheader('Scatter Matrix')
    fig = px.scatter_matrix(df, dimensions=['price', 'model_year', 'odometer', 'days_listed', 'cylinders'], title='Scatter Matrix')
    st.plotly_chart(fig)

