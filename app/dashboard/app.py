import streamlit as st
import pandas as pd
from app.analytics.scoring import add_score
from app.copilot.service import ask

st.set_page_config(page_title="KAPASITA-MVP", layout="wide")
st.title("KAPASITA — AI Policy Intelligence")
st.caption("Sekolah Rakyat & Pendidikan Inklusif | MVP LAN Datathon 2026")
st.info("Fokus MVP: layanan inklusif, intervensi kebijakan, dan kapasitas. Bukan penentuan lokasi Sekolah Rakyat.")

uploaded = st.file_uploader("Demo: upload master dataset CSV", type=["csv"])
if uploaded:
    df = add_score(pd.read_csv(uploaded))
    st.dataframe(df.sort_values("SR_ICSS", ascending=False), use_container_width=True)
    q = st.text_input("Tanyakan hasil analisis")
    if q:
        context = df.head(20).to_json(orient="records")
        st.write(ask(q, context))
else:
    st.write("Untuk mode produksi MVP, hubungkan ingestion Google Drive sebelum deployment.")
