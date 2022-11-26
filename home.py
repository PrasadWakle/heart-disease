import streamlit as st
import numpy as np
import pandas as pd

def main():
    st.title('Heart Disease Prediction Web App')
    
    st.markdown("""According to the Centers for Disease Control and Prevention (CDC), about 610,000 people die of heart disease in the United States every year–that’s 1 in every 4 deaths. Heart disease is the leading cause of death for both men and women. 

Logistic regression is a statistical method for classifying data into two groups. It can be used to predict whether a patient has heart disease, based on a set of symptoms. The accuracy of logistic regression varies, depending on the data set. This project aims to predict whether a person has heart disease with the help of Logistic Regression.""")

    df=pd.read_csv(r'heart_disease_data.csv')

    st.subheader('Training Data')
    st.write(df.describe())

   