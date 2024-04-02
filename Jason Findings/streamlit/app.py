import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt


def _get_list_universities_name():
    university_names = ["University of Washington", "Carnegie Mellon University"]
    return university_names

"""
selectbox()
arguments:
- options= | Labels for the select options in an Iterable. For example, this can be a list, 
numpy.ndarray, pandas.Series, pandas.DataFrame, or pandas.Index. For pandas.DataFrame, 
the first column is used. Each label will be cast to str internally by default.
"""
def _get_major_by_university(university_name: str):

    print("university name: ", UNIVERSITY_NAME)
    if university_name == "University of Washington":
        return ["Informatics", "CSE", "Data Science"]
    else:
        return ["None"]

def _normalize_toefl_ielts_score(score: int):
    normalized_score = 0

    
    if score <= 9: #IELTS
        normalized_score = score / 9 * 10
    else: #TOEFL
        normalized_score = score / 120 * 10
    return normalized_score

st.write("Hello World, Mining Men!!")

#'GPA', 'GRE Total', 'TOEFL', 'Work Exp', 'Papers'
#issueL TOEFL/IELTS | 
    #TOEFL = x / 120 * 10
    #IELTS = x / 9 * 10
with st.form("user_input"):
    st.write(":red[\* Indicates required question]", )
    GPA = st.number_input("Enter GPA score* [0.0 - 4.0]:", value=3.0, min_value=1.0, max_value=4.0, step=0.1, placeholder="0.0 - 4.0")
    GRE = st.number_input("Enter GRE score* [260 - 340]: ", value=300, min_value=260, max_value=340, step=1, placeholder="260 - 340")
    TOEFL_IELTS = st.number_input("Enter TOEFL [0-120] / IELTS [0-9] score*: ", value=100, min_value=0, max_value=120, step=1, placeholder="TOEFL [0-120] or IELTS [0-9]") #TOEFL: 0-120 IELTS: 0-9 
    #st.write("years of work experience")
    WORK_EXPERIENCE = st.number_input("Working experience (years): ",  min_value=0, max_value=100, step=1)
    
    #dropdown on what universities list
    #University name
    #UNIVERSITY_NAME = st.text_input(placeholder="Enter University Name", label="University Name*", value="University of Washington")
    #University name -> Major
    UNIVERSITY_NAME = st.selectbox(options=_get_list_universities_name(), label="Select your University to apply: ")
    #Labels for the select options in an Iterable. For example, this can be a list, numpy.ndarray, pandas.Series, pandas.DataFrame, or pandas.Index. For pandas.DataFrame, the first column is used. Each label will be cast to str internally by default.
    UNIVERSITY_MAJOR = st.selectbox(options=_get_major_by_university(UNIVERSITY_NAME), label="Enter your Major*" )
    user_input_submitted = st.form_submit_button(label="Predict Button")

    if user_input_submitted:
        #user_input = [GPA, GRE, TOEFL_IELTS, WORK_EXPERIENCE, UNIVERSITY_NAME, UNIVERSITY_MAJOR]
        NORMALIZED_TOEFL_IELTS = _normalize_toefl_ielts_score(TOEFL_IELTS)
        st.write(NORMALIZED_TOEFL_IELTS)


