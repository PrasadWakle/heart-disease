import numpy as np
import pickle


# loading the saved model
loaded_model = pickle.load(open('C:/Users/prasa/OneDrive/Desktop/Heart/trained_model.sav', 'rb'))


input_data = (67,1,0,160,286,0,0,108,1,1.5,1,3,2)

# change the input data to a numpy array
input_data_as_numpy_array= np.asarray(input_data)

# reshape the numpy array as we are predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]== 0):
  print('The Person does not have a Heart Disease')
else:
  print('The Person has Heart Disease')









