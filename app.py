import streamlit as st

if "kibun_history" not in st.session_state:
    st.session_state["kibun_history"] = []


col1, col2, col3, col4 = st.columns(4)
with col1:
     if st.button("楽しい"):
        st.session_state.[kibun_history].append("楽しい")
with col2:
     if st.button("悲しい"):
        st.session_state.[kibun_history].append("悲しい")
with col3:
     if st.button("眠い"):
        st.session_state.[kibun_history].append("眠い")
with col4:
     if st.button("おなかすいた"):
        st.session_state.[kibun_history].append("おなかすいた")

for kibun in st.session_state["kibun_history"]:
    st.write(kibun)
