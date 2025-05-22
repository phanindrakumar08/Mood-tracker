import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, date
import pandas as pd
import plotly.express as px


SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", SCOPE)
client = gspread.authorize(CREDS)

@st.cache_data(ttl=60)
def load_sheet_data():
    sheet = client.open("Mood Tracker").sheet1
    return sheet.get_all_records()


st.title("Mood Tracker")

mood = st.selectbox("How are you feeling today?", ["😊 Happy", "😠 Angry", "😕 Meh", "🎉 Excited", "🧘🏻‍♀️ Peaceful"])
note = st.text_input("Optional note (e.g., 'Lot of traffic')")

if st.button("Submit Mood"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet = client.open("Mood Tracker").sheet1
    sheet.append_row([timestamp, mood, note])
    st.success("Mood logged!")
    st.rerun()  

raw_data = load_sheet_data()
data = pd.DataFrame(raw_data)

if not data.empty:
    if 'Timestamp' in data.columns:
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])
        data['Date'] = data['Timestamp'].dt.date
        data['Mood'] = data['Mood'].str.extract(r'(\w+)$')

        today = date.today()
        today_data = data[data['Date'] == today]

        
        if not today_data.empty:
            st.subheader("📊 Today's Mood Summary")
            mood_counts = today_data['Mood'].value_counts().reset_index()
            mood_counts.columns = ['Mood', 'Count']
            fig = px.bar(mood_counts, x='Mood', y='Count', color='Mood',
                         title=f"Mood Count for {today}", labels={'Count': 'Number of Entries'})
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No mood data logged for today yet.")
    else:
        st.warning("⚠️ 'Timestamp' column is missing in the sheet.")
else:
    st.info("No mood entries found. Start by logging your mood!")
