import streamlit as st
from datetime import datetime

# Function to calculate difference in minutes
def calculate_time_difference(start_time, end_time):
    time_start = datetime.strptime(start_time, "%H:%M")
    time_end = datetime.strptime(end_time, "%H:%M")
    difference = (time_end - time_start).seconds / 60
    return difference

# Updated function to convert minutes to hours and minutes
def convert_minutes_to_hours_and_minutes(minutes):
    hours = minutes // 60  # Full hours
    remainder_minutes = minutes % 60  # Remaining minutes
    return hours, remainder_minutes

# Setting page config to add a title and icon
st.set_page_config(page_title="TimeCraft - Time Management Tools", page_icon="⏰")

# Header for the entire app
st.header("TimeCraft - Time Management Tools")

# Creating tabs
tab1, tab2 = st.tabs(["Time Difference Calculator", "Minutes to Hours Converter"])

with tab1:
    st.subheader("Calculate Time Difference")
    
    # User inputs for time
    start_time = st.time_input("Start Time", key="start")
    end_time = st.time_input("End Time", key="end")
    
    if st.button("Calculate Difference", key="diff"):
        # Formatting times for the function
        start_time_str = start_time.strftime("%H:%M")
        end_time_str = end_time.strftime("%H:%M")
        difference = calculate_time_difference(start_time_str, end_time_str)
        st.write(f"The difference is {difference} minutes.")

with tab2:
    st.subheader("Convert Minutes to Hours and Minutes")
    
    # User input for minutes
    minutes = st.number_input("Enter minutes", min_value=0, step=1, key="min")
    
    if st.button("Convert", key="conv"):
        hours, remainder_minutes = convert_minutes_to_hours_and_minutes(minutes)
        st.write(f"{minutes} minutes is approximately {hours} hours and {remainder_minutes} minutes.")

# Adding developer's name
st.sidebar.markdown("### Developed by Aditya")
