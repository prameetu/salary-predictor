import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_step.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data['model']
le_country = data['le_country']
le_edu  = data['le_education']

def predict_page():
    st.title('SOFTWARE DEVELOPER SALARY PREDICTION')
    st.write("""###### *All data is based on Stack Overflow Survey 2020""")
    st.write(" ")
    st.write(" ")


    st.write("""### Enter the details below to get your predicted salary """)
    st.write(" ")

    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )

    education = (
        "Less than a bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post Grad",
    )

    country = st.selectbox("Country",countries)
    edu_level = st.selectbox("Education Level",education)

    experience = st.slider("Years of Experience",0,50,3)

    ok = st.button("Get Salary")

    if ok:
        ip = np.array([[country, edu_level, experience]])
        ip[:, 0] = le_country.transform(ip[:, 0])
        ip[:, 1] = le_edu.transform(ip[:, 1])
        ip = ip.astype(float)

        salary = regressor.predict(ip)
        st.header(f'Your estimated salary is ${salary[0]:.2f}')