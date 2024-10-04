import streamlit as st
import pickle as pkl

with open('p5Model1.pkl','rb') as f1:
    model = pkl.load(f1)

st.title("Weight Prediction App")

height = st.text_input("Enter your Height")

if st.button("Predict"):
    if height:
        height = float(height)
        prediction = model.predict([[height]])
        st.write(f"Predicted weight {prediction[0]}")
    else:
        st.write('Please Enter the valid Height')
    