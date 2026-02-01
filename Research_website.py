# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 15:04:42 2026

@author: Tshidiso Mazibuko
"""

import streamlit as st
import plotly.express as px
import pandas as pd


name = "Tshidiso Mazibuko"
field = "Machine Learning"
Institution = "University of South Africa (UNISA)"


st.header("Research Overview")
st.write(f"Name: {name}")
st.write(f"Field of research: {field}")
st.write(f"Institution: {Institution}")

st.header("Research outline")
multi = '''This main focus area of this research is on the plant-wide fault detection of the Tenessee Eastman chemical process (TEP)
with 20 simulated faults. Three machine learning algorithms were investigated. These algorithms are the vanilla neural network autoencoder, the 
dynamic neural network autoencoder and the Long Short Term Memory (LSTM) autoencoder. The metric used in measuring the accuracy of the alogithms was the 
fault detection rate (FDR), also known as the true positive rate. Since artficial neural networks are non deterministic models in their nature,
30 (or more) independent runs were carried out for each fault so as to gain statistical insight into the performance of each algorithm.'''
st.markdown(multi)

# Load data
df_autoencoder = pd.read_excel("Book1.xlsx","Autoencoder")
df_Dyautoencoder = pd.read_excel("Book1.xlsx","Dynamic autoencoder")
df_LSTMautoencoder = pd.read_excel("Book1.xlsx","LSTM autoencoder")


st.header("Results Explorer")
# Load data
df_autoencoder = pd.read_excel("Book1.xlsx","Autoencoder")
df_Dyautoencoder = pd.read_excel("Book1.xlsx","Dynamic autoencoder")
df_LSTMautoencoder = pd.read_excel("Book1.xlsx","LSTM autoencoder")

st.subheader("Results viewer")
data_option = st.selectbox("Choose the results of the machine learning algorithm", [
    "Autoencoder", "Dynamic autoencoder","LSTM autoencoder"]
    )
if data_option == "Autoencoder":
    st.write("### Autoencoder results: FDR(%)")
    st.dataframe(df_autoencoder)
    df_melted = df_autoencoder.melt(id_vars=["Run"], var_name="Fault", value_name="Fault detection rate (%)")
    #st.dataframe(df_melted )
    fig = px.box(df_melted, x="Fault", y="Fault detection rate (%)", points="all", title="Fault-wise Box Plots")
    st.plotly_chart(fig)
    
   #fig.show()

elif data_option == "Dynamic autoencoder":
    st.write("### Dynamic Autoencoder results: FDR(%)")
    st.dataframe(df_Dyautoencoder)
    df_melted = df_Dyautoencoder.melt(id_vars=["Run"], var_name="Fault", value_name="Fault detection rate (%)")
    #st.dataframe(df_melted )
    fig = px.box(df_melted, x="Fault", y="Fault detection rate (%)", points="all", title="Fault-wise Box Plots")
    st.plotly_chart(fig)
    
elif data_option == "LSTM autoencoder":
    st.write("### LSTM Autoencoder results: FDR(%)")
    st.dataframe(df_LSTMautoencoder)
    df_melted = df_LSTMautoencoder.melt(id_vars=["Run"], var_name="Fault", value_name="Fault detection rate (%)")
    #st.dataframe(df_melted )
    fig = px.box(df_melted, x="Fault", y="Fault detection rate (%)", points="all", title="Fault-wise Box Plots")
    st.plotly_chart(fig)
    
#Add contact information
st.header("Contact Information")
email = "tshidisomazibuko@gmail.com"
st.write(f"You can reach me on: {email}")
