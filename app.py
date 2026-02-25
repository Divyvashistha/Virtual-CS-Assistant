import streamlit as st
from engine import generate_response

st.set_page_config(page_title="CS Assistant", layout="wide")

st.title("CS Assistant")
st.write("Internal working note generator for Companies Act & compliance issues.")

query = st.text_area(
    "Describe the issue / task:",
    height=200,
    placeholder=""
)

if st.button("Generate Internal Note"):
    if query.strip() == "":
        st.warning("Please enter a problem.")
    else:
        with st.spinner("Analyzing like a Company Secretary..."):
            result = generate_response(query)
        st.success("Draft Ready")
        st.text_area("Internal Working Note", result, height=400)