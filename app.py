import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Happy New Year!", page_icon="🥳")

THIS_DIR = Path(__file__).parent
page2k25 = THIS_DIR / "views" / "2025.py"
page2k24 = THIS_DIR / "views" / "2024.py"


page2024 = st.Page(
    page = page2k24,
    title = "2024",
    icon = "💙",
)

page2025 = st.Page(
    page = page2k25,
    title = "2025",
    icon = "🩷",
    default=True,
)

pg = st.navigation(pages=[page2025, page2024])
logo_path = "assets/logo.png"
st.logo(logo_path)
st.sidebar.text("HI THERE HOTTIE😍😍")
st.sidebar.image(logo_path, width=200)  # Adjust the width as needed

pg.run()
