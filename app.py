import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd  # Import pandas for DataFrame
import requests  # Import requests for API calls

# Function to fetch data from an API
def fetch_data(endpoint):
    try:
        response = requests.get(endpoint)  
        response.raise_for_status()  # Raises an error for bad responses (4xx, 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None

# Function to send data via POST request
def send_data(name, gender, age, favorite_number):
    api_url = "http://127.0.0.1:5501/api/customers/"  # Ensure this matches your Django API
    payload = {
        "name": name,
        "gender": gender,
        "age": age,
        "favorite_number": favorite_number
    }

    try:
        response = requests.post(api_url, json=payload)
        return response
    except requests.exceptions.RequestException as e:
        st.error(f"Error sending data: {e}")
        return None

st.title("Analytics Dashboard")
st.write("v.0.0.1")

col1, col2 = st.columns([1, 1])  # Equal width columns

st.write("Some content")  # Fixed indentation

# Using expander properly
with st.expander("Click to choose something"):
    st.write("Option to choose")
    st.write("Another option to choose")

with col1:
    st.write("### Column 1")  

with col2:
    st.write("### Column 2")  

# Data for the bar chart
categories = ['A', 'B', 'C', 'D']
values = np.random.randint(10, 100, size=(4,))

# Creating a Matplotlib figure
fig, ax = plt.subplots()

# Bar chart
ax.bar(categories, values, color='blue')

# Labels and title
ax.set_xlabel('Categories')
ax.set_ylabel('Values')
ax.set_title('First Bar Chart')

# Displaying the chart in Streamlit
st.pyplot(fig)

# Session state for counter
if 'counter' not in st.session_state:
    st.session_state.counter = 0

if st.button("Increase Counter"):
    st.session_state.counter += 1

st.write(f"Counter Value: {st.session_state.counter}")

# Fetching data from SWAPI
swapi_endpoint = "https://swapi.dev/api/people/1/"
swapi_data = fetch_data(swapi_endpoint)

if swapi_data:
    st.write("### Star Wars Character Data")
    st.json(swapi_data)  # Displays fetched data in JSON format

# Fetch data from Django API
api_url = "http://127.0.0.1:5501/api/customers/"  # Fixed port
data = fetch_data(api_url)

if data:
    df = pd.DataFrame(data)  # Convert API data to DataFrame
    st.write("### Customers Data")
    st.dataframe(df)  # Display DataFrame in Streamlit

    # Scatter Plot using Streamlit
    st.write("### Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(df.index, df.iloc[:, 1], color='red', label="Values")  # Adjust column index if needed
    ax.set_xlabel("Index")
    ax.set_ylabel("Values")
    ax.set_title("Scatter Chart")
    ax.legend()

    # Display scatter plot
    st.pyplot(fig)

# Form to collect customer data
st.write("## Submit Your Data")
name = st.text_input("Your Name")
gender = st.radio("Select Your Gender", ["Male", "Female"])
age = st.slider("Select Your Age", 1, 100, 18)
favorite_number = st.number_input("Enter Your Favorite Number", step=1)

if st.button("Submit"):
    response = send_data(name, gender, age, favorite_number)
    
    if response and response.status_code == 201:
        st.success("Data submitted successfully!")
    else:
        st.error("Something went wrong.")
