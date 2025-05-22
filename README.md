# Loom Walkthrough - https://www.loom.com/share/fca50839102b40bcb865cc5e3efbf0c4?sid=8ab5fc8b-6d9c-4516-bded-65f8a0b28e7a

Google Sheet - https://docs.google.com/spreadsheets/d/1nSBKCiQ1Ti1c21NU7hqAK8tl2Tp4aigCeYXrpJezABw/edit?usp=sharing

# 🧠 Mood Tracker

![image](https://github.com/user-attachments/assets/55c6e81e-766a-4a15-8715-986f3d2babef)

A simple and interactive web application built with **Streamlit** and **Google Sheets API** that helps you track and visualize your daily moods. Log how you're feeling, optionally add a note, and see a live chart of your mood trends for the day.

---

## 🚀 Features

- Log daily moods with a timestamp
- Optional notes for context
- Store entries in Google Sheets
- Auto-refresh and cache data to prevent API quota exhaustion
- Visualize today's mood distribution using Plotly charts
- Lightweight and easy to deploy

---

## 📸 Demo

![Mood Tracker Demo](demo.gif) <!-- Optional: Add if you record a gif or screenshot -->

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [Google Sheets API](https://developers.google.com/sheets/api)
- [gspread](https://github.com/burnash/gspread)
- [oauth2client](https://github.com/googleapis/oauth2client)
- [pandas](https://pandas.pydata.org/)
- [plotly](https://plotly.com/python/)

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/mood-tracker.git
cd mood-tracker
