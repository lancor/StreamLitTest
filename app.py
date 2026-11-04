import requests
import streamlit as st
 
st.title('New Haven: 7-day forecast')
 
url = 'https://api.open-meteo.com/v1/forecast'
params = {
    'latitude': 41.31,
    'longitude': -72.92,
    'daily': 'temperature_2m_max',
    'temperature_unit': 'fahrenheit',
    'timezone': 'America/New_York',
}
response = requests.get(url, params=params)
data = response.json()
days = data['daily']['time']
highs = data['daily']['temperature_2m_max']
 
st.subheader('Daily high temperature (°F)')
st.bar_chart({'day': days, 'high': highs}, x='day', y='high')

