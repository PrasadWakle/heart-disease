import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))


# creating a function for Prediction

def heartDiseasePrediction(input_data):
    

    # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)

    # reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 0):
        return('The Person does not have a Heart Disease')
    else:
        return('The Person has Heart Disease')
  
    
  
def main():
    
    
    # giving a title
    st.title('Heart Disease Prediction Web App')
    
    
    # getting the input data from the user
    
    
    Age = st.text_input('Age of Person')
    Sex = st.text_input('Sex of Person (1 = Male, 0 = Female)')
    CP = st.text_input('Chest Pain Type')
    Trestbps = st.text_input('Resting Blood Pressure')
    Chol = st.text_input('Serum Cholestoral in mg/dl')
    Fbs = st.text_input('Fasting Blood Sugar')
    Restecg = st.text_input('Resting Electrocardiographic Results')
    Thalach = st.text_input('Maximum Heart Rate Achieved')
    Exang = st.text_input('Exercise Induced Angina')
    Oldpeak = st.text_input('Oldpeak')
    Slope = st.text_input('ST Slope')
    CA = st.text_input('CA (Number of major vessels (0-3) colored by flourosopy)')
    Thal = st.text_input('Thal')
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    try:
        if st.button('Test Result'):
          diagnosis = heartDiseasePrediction([Age,Sex,CP,Trestbps,Chol,Fbs,Restecg,Thalach,Exang,Oldpeak,Slope,CA,Thal])
        
        
        st.success(diagnosis)

    except:st.error('All fields are mandatory')
    
    
    
    
    
if __name__ == '__main__':
    main()