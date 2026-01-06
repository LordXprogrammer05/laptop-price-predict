import streamlit as st
import pickle
import numpy as np

# importing the model
pipe = pickle.load(open('pipe.pkl' , 'rb'))
df =pickle.load(open('df.pkl' , 'rb'))

st.title("Laptop Predictor")

# brand
Brand = st.selectbox('Brand' , df['Company'].unique())

# type of Laptop
Type = st.selectbox('Type' , df['TypeName'].unique())

#Ram
RAM = st.selectbox('RAM' , [2,4,6,8,12,16,24,32,64])

# Weight
weight = st.number_input("Enter laptop weight (in kg)")


# Touchscreen 
Touchscreen = st.selectbox('Touchscreen' , ['No' , 'Yes'])
if Touchscreen == 'Yes':
    Touchscreen = 1
else:
    Touchscreen = 0

#IPS
ips = st.selectbox('IPS' , ['NO' , 'Yes'])

#Gpu brand
Gpu = st.selectbox('GPU' , df['Gpu brand'].unique())

# CPU brand

Cpu = st.selectbox('CPU' , df['Cpu brand'].unique())

# HDD
HDD = st.selectbox('HDD' , [0,128,256,512,1824,2848])

# SSD
SSD = st.selectbox('SSD' , [0,128,256,512,1824,2848])

# OS
os = st.selectbox('Os' , df['os'].unique())



ips = 0
query = np.array([Brand, Type, RAM, weight, Touchscreen,
                      ips, Gpu, Cpu, HDD, SSD, os])
        


query = query.reshape(1,11)
st.title("The predicted Price of this Type of Laptop"    + str(int(np.exp(pipe.predict(query)[0]))))