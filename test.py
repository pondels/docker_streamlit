import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set page title
st.set_page_config(page_title='Streamlit Demo')

# Create a title and description
st.title('Streamlit Demo App')
st.write('This is a simple Streamlit application demonstrating various elements.')

# Create a button
if st.button('Click Me'):
    st.write('Button clicked!')

# Create a dropdown
option = st.selectbox('Select an option', ['Option 1', 'Option 2', 'Option 3'])
st.write('You selected:', option)

# Create a slider
value = st.slider('Select a value', 0, 10)
st.write('Selected value:', value)

# Create a checkbox
if st.checkbox('Check me out'):
    st.write('Checkbox is checked!')

# Create a text input
name = st.text_input('Enter your name')
st.write('Hello', name)

# Create a dataframe
data = {'x': np.random.randn(100), 'y': np.random.randn(100)}
df = pd.DataFrame(data)

# Create a line chart
st.line_chart(df)

# Create a bar chart
st.bar_chart(df)

# Create a scatter plot
st.scatter_chart(df)

# Create a button to download data
if st.button('Download Data'):
    st.download_button(
        label='Download CSV',
        data=df.to_csv().encode('utf-8'),
        file_name='data.csv',
        mime='text/csv'
    )
