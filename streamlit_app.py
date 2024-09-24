import streamlit as st

st.title("Calendar")
st.write(
    "Have a question about coding? Book time with Feng and Aine!")

import calendar
from datetime import datetime

# Set page title
st.title("Calendar Viewer")

# Get the current date
today = datetime.today()
current_year = today.year
current_month = today.month

# Function to display a calendar
def display_calendar(year, month):
    # Create an instance of TextCalendar class
    cal = calendar.TextCalendar(calendar.SUNDAY)
    cal_str = cal.formatmonth(year, month)
    # Display the calendar in the Streamlit app
    st.text(cal_str)

# Sidebar to select year and month
st.sidebar.header("Select Year and Month")
selected_year = st.sidebar.number_input('Year', min_value=1900, max_value=2100, value=current_year)
selected_month = st.sidebar.selectbox('Month', list(calendar.month_name)[1:], index=current_month - 1)

# Display the calendar for the selected year and month
display_calendar(selected_year, list(calendar.month_name).index(selected_month))

#Build a bot that mirrors your input
import streamlit as st

st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
