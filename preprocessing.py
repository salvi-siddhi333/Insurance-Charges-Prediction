# Import modules
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


@st.cache
def load_data():
    # Load the dataset
    df = pd.read_csv("kaggle_insurance.csv")

    # Change values to numerical
    df.replace(to_replace={"male":0, "female":1, "no":0, "yes":1, "northwest": 0, "northeast":1, "southeast":2, "southwest":3}, inplace=True)

    #1-hot encoding
    df = pd.get_dummies(df)

    # Split data into feature and target
    X = df.drop(['charges'], axis=1)
    y = df['charges']

    # Return values
    return X,y


@st.cache
def acc():
    #load features and target
    X,y = load_data()

    #create model and accuracy
    model = LinearRegression()
    model.fit(X,y)
    acc = model.score(X,y)

    #return accuracy
    return model,acc