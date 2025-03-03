import streamlit as st
import pandas as pd
import plotly.express as px

def load_data():
    return pd.read_csv("data/data.csv")

def show_visualize():
    st.title("Visualize")
    data = load_data()
    
    st.subheader("Visualizations")
    
    # Example visualizations
    fig1 = px.histogram(data, x='radius_mean', title='Radius Mean Distribution')
    st.plotly_chart(fig1)
    
    fig2 = px.scatter(data, x='radius_mean', y='texture_mean', color='diagnosis', title='Radius Mean vs Texture Mean')
    st.plotly_chart(fig2)

def main():
    show_visualize()

if __name__ == '__main__':
    main()