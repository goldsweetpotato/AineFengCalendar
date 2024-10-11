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

# gcsa imports
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA
from google.oauth2 import service_account

# misc imports
from beautiful_date import Jan, Apr, Sept, Oct
import json
import os
from datetime import date, datetime
from beautiful_date import hours

# langchain imports
from langchain_core.runnables.utils import ConfigurableFieldSpec
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents.react.agent import create_react_agent
from langchain_core.output_parsers import StrOutputParser
from langchain_core.tools import Tool, StructuredTool  # Use the Tool object directly
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain_community.chat_message_histories import (
    StreamlitChatMessageHistory,
)
from langchain_community.callbacks.streamlit import (
    StreamlitCallbackHandler,
)
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
from langchain.callbacks.tracers import ConsoleCallbackHandler
from pydantic import BaseModel, Field


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

# Prompt

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
