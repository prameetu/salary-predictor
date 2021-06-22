import streamlit as st
import  pandas as pd
import  matplotlib.pyplot as plt


def clean_data(col,threshold):
    countries = {}
    for i in range(len(col)):
        if col.values[i] >= threshold:
            countries[col.index[i]] = col.index[i]
        else:
            countries[col.index[i]] = 'Other'
    return countries

def clean_experience(col):
    if col == 'More than 50 years':
        return 50
    if col == 'Less than 1 year':
        return 0.5
    return float(col)

def clean_education_level(col):
    if "Bachelor’s degree" in col:
        return 'Bachelor’s degree'
    if "Master’s degree" in col:
        return "Master’s degree"
    if 'Professional degree' in col or 'Other doctoral' in col:
        return 'Post Grad'
    return 'Less than a bachelors'

@st.cache
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedComp"]]
    df = df.rename({'ConvertedComp': 'Salary'}, axis=1)
    df = df[df["Salary"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed full-time"]
    df = df.drop("Employment", axis=1)

    country_map = clean_data(df.Country.value_counts(), 400)
    df["Country"] = df["Country"].map(country_map)
    df = df[df["Salary"] <= 250000]
    df = df[df["Salary"] >= 10000]
    df = df[df["Country"] != "Other"]

    df['Experience'] = df['YearsCodePro'].apply(clean_experience)
    df = df.drop('YearsCodePro', axis=1)
    df['Education_Level'] = df['EdLevel'].apply(clean_education_level)
    df = df.drop('EdLevel', axis=1)
    return df


df = load_data()

def show_explore_page():

    st.title('EXPLORING SOFTWARE DEVELOPER SALRIES')
    st.write("""###### *All data is based on Stack Overflow Survey 2020""")
    st.markdown('***')


    data = df["Country"].value_counts()
    fig1, ax1 = plt.subplots(figsize = (15,10))
    ax1.pie(data, labels=data.index, autopct="%1.1f%%")
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.write("""#### Number of data from different countries""")
    st.write("")
    st.pyplot(fig1)

    st.markdown('***')

    st.write("""#### Mean Salary Based on Country""")
    st.write("")
    st.write("")


    data = df.groupby(['Country'])['Salary'].mean().sort_values(ascending=True)
    st.bar_chart(data,100,400,use_container_width=True)

    st.markdown('***')

    st.write("""#### Mean Salary Based on Experience""")
    st.write("")
    st.write("")

    data = df.groupby(['Experience'])['Salary'].mean().sort_values(ascending=True)
    st.line_chart(data)