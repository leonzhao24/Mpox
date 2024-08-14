import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Load your data
@st.cache
def load_data(file_path):
    return pd.read_csv(file_path)

# Assuming the data is already filtered to focus on Austin
data_path = '/path/to/your/tweets.csv'
df = load_data(data_path)

# Header
st.title("Mpox Dashboard")

# Navigation Links
st.markdown("""
<nav>
    <a href='#methodology'>Our Methodology</a> |
    <a href='#mission'>Our Mission</a> |
    <a href='#advanced-search'>Advanced Search for Tweets</a>
</nav>
""", unsafe_allow_html=True)

# Counters
total_tweets = len(df)
cases_in_austin = 50  # Example, replace with actual data

st.metric("Total number of Mpox Tweets:", total_tweets)
st.metric("Total number of cases in Austin:", cases_in_austin)

# Sidebar: List of Keywords
st.sidebar.title("List of Keywords")
keywords = ["Monkey", "Pox", "Quarantine", "Crazy"]
counts = {"Monkey": 10000, "Pox": 10000, "Quarantine": 10000, "Crazy": 10000}  # Replace with actual counts

for keyword in keywords:
    st.sidebar.write(f"{keyword}:")
    st.sidebar.write(f"Last month: {3000}")  # Replace with actual monthly counts
    st.sidebar.write(f"Total: {counts[keyword]}")

# Map Visualization
st.subheader("Graph above shows the geographic location of the tweets in Austin")
if 'latitude' in df.columns and 'longitude' in df.columns:
    fig = px.scatter_mapbox(df, lat='latitude', lon='longitude', hover_name='text',
                            mapbox_style='carto-positron', zoom=10, height=500)
    st.plotly_chart(fig)
else:
    st.write("Geolocation data is not available.")

# Line Chart: Frequency of tweets over time by topic
st.subheader("Frequency of tweets over time by topic")
fig, ax = plt.subplots()
for keyword in keywords:
    # Generate fake time series data (replace with your actual data)
    time_series = df['date'].value_counts().sort_index()
    ax.plot(time_series, label=keyword)

ax.set_xlabel("Date")
ax.set_ylabel("Number of Tweets")
ax.legend()
st.pyplot(fig)

# Link to the paper
st.subheader("Link to our paper:")
st.markdown("[Click here to read our paper](https://example.com)", unsafe_allow_html=True)

# Advanced Search Section
st.markdown("<h2 id='advanced-search'>Advanced Search for tweets</h2>", unsafe_allow_html=True)
st.text_input("Key Terms", "")
st.date_input("Time period", [])
st.text_input("Engagement")
st.selectbox("Topic Labels", ["Anxious", "Happy", "Neutral"])
st.button("Submit advanced Search")
