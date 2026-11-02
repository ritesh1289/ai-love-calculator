
import streamlit as st
import random

st.set_page_config(
    page_title="Love Calculator",
    page_icon="❤️"
)

st.title("💖 LOVE CALCULATOR 💖")
st.subheader("Ritesh & Soniya Special Edition")

name1 = st.text_input("Enter First Name")
name2 = st.text_input("Enter Second Name")

if st.button("💘 Calculate Love 💘"):

    if not name1.strip() or not name2.strip():
        st.warning("Please enter both names.")

    else:
        first = name1.strip().lower()
        second = name2.strip().lower()

        special_pairs = [
            ("ritesh", "soniya"),
            ("shiv", "parvati"),
            ("romeo", "juliet")
        ]

        if (first, second) in special_pairs or (second, first) in special_pairs:
            score = 100
        else:
            random.seed(first + second)
            score = random.randint(0, 100)

        st.metric("❤️ Love Score", f"{score}%")
        st.progress(score)

        if score >= 80:
            st.success("💞 True Love! A beautiful connection!")
        elif score >= 50:
            st.info("💕 A lovely connection!")
        elif score >= 30:
            st.warning("💗 Keep building your relationship!")
        else:
            st.write("😊 Friendship is also special!")
