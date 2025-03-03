import streamlit as st
import data
import visualize
import predict

def show_home():
    st.title("Breast Cancer Prediction App")
    st.subheader("By Taufeeq Riyaz - 1RVU23CSE506")

def main():
    st.set_page_config(
        page_title="Breast Cancer Predictor",
        page_icon="🎀",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    with open("assets/style.css") as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    
    tabs = st.tabs(["Home", "Data", "Predict", "Visualize"])
    
    with tabs[0]:
        show_home()
    
    with tabs[1]:
        data.main()
    
    with tabs[2]:
        predict.main()
    
    with tabs[3]:
        visualize.main()

if __name__ == '__main__':
    main()