from AI_Component.Crew import *
import Component.Logo as Img
import streamlit as st

Img.image(["./Image/gema.png", "./Image/Unpad.png"])
st.title("AI PERIKANAN GEMA UNPAD")
st.write("Berikut adalah pusat informasi yang dikembangkan oleh GEMA dan UNPAD, menggunakan data-data yang ")

input = st.text_input("Masukkan pertanyaan")
lang = st.text_input("Bahasa")
submit = st.button("Cari")

if submit:
    result = KokoaCrew(input, lang).generalCrew().kickoff()
    st.markdown(result)