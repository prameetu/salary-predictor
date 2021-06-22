import streamlit as st
import base64
from predict_page import predict_page
from explore_page import  show_explore_page
page = st.sidebar.selectbox('EXPLORE or PREDICT',['Explore','Predict'])

main_bg = "sample.jpg"
main_bg_ext = "jpg"

side_bg = "sample.jpg"
side_bg_ext = "jpg"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
   .sidebar .sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)

if(page == 'Predict'):
    predict_page()
elif(page == 'Explore'):
    show_explore_page()