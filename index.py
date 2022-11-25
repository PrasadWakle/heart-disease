import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))


# creating a function for Prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
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
    
    
    Age = st.text_input('Age of the Person')
    Sex = st.text_input('Sex of the Person')
    CP = st.text_input('Chest Pain Type (CP)')
    Trestbps = st.text_input('Resting Blood Pressure (trestbps)')
    Chol = st.text_input('Serum Cholestoral in mg/dl')
    Fbs = st.text_input('Fasting Blood Sugar (fbs)')
    Restecg = st.text_input('Resting Electrocardiographic Results (restecg)')
    Thalach = st.text_input('Maximum Heart Rate Achieved (thalach)')
    Exang = st.text_input('Exercise Induced Angina (exang)')
    Oldpeak = st.text_input('Oldpeak')
    ST_Slope = st.text_input('ST Slope (The slope of the peak exercise ST segment)')
    CA = st.text_input('Number of major vessels (0-3) colored by flourosopy')
    Thal = st.text_input('Thal')
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    try:
        if st.button('Test Result'):
          diagnosis = diabetes_prediction([Age,Sex,CP,Trestbps,Chol,Fbs,Restecg,Thalach,Exang,Oldpeak,ST_Slope,CA,Thal])
        
        
        st.success(diagnosis)

    except:st.error('All fields are mandatory')
    
    
    
    
    
if __name__ == '__main__':
    main()