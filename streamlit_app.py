import streamlit as st
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA

from beautiful_date import Jan, Apr, Sept
import json
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA
from google.oauth2 import service_account
from beautiful_date import Jan, Apr, Sept


# Deviations from documentation:
# 1- Creating service account and then creating a key for it. (because we the app can't create a server for itself).
# 2- Adding the service account email to your calendar as a user with event edit permissions (from Settings and Sharing) (because we the app can't create a server for itself).
# 3- Using service_account.Credentials.from_service_account_info to get the credenntials instead of credentials_path (for security reasons).
# 4- Putting the JSON in StreamLit secrets and using json.loads rather than uploading the file to github (for security reasons).


# Get the credintials from Secrets.
credentials = service_account.Credentials.from_service_account_info(
        json.loads(st.secrets["FengJson"]),
        scopes=["https://www.googleapis.com/auth/calendar"]
    )

# Create the GoogleCalendar.
calendar = GoogleCalendar(credentials=credentials)

# Get the list of events.
c = list(calendar.get_events(calendar_id="mflin@bu.edu"))

# It erate through the events and show them.
for event in c:
    st.write(event)
