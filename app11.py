from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title='My Webpage', page_icon=':tada:', layout='wide')
st.subheader('Hello! :wave: We are team 55 and this is our final project about NYC Airbnb Listings')
st.title("NYC Airbnb Listings")
st.write('Dimitar Dimitrov, Myria Stavrou, Iris Toetenel, Haneul Choi')


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl('https://assets7.lottiefiles.com/packages/lf20_1CKhDgcctU.json')


with st.container():
        st.write('---')
        left_column, right_column = st.columns(2)
        with left_column:
            st.header('Goal')
            st.write(
                '''
                Our main goal is to provide insights for the current and potential hosts of Airbnb, so that they know where to invest, after discovering the influential factors for the users.
                '''
            )
            st.write('##')
            st.header('Context')
            st.write(
                '''
                In our project we created interactive plots in order to discover:
                - distribution of values for each attribute
                - relationships/correlation between different attributes
                - patterns
                - trends
                - whether external data, such as Airbnb's distances from subway stations and NYC center affect the price or any other attribute

                If this sounds interesting to you, and you want to check the visualizations, you can continue by clicking:
                '''
            )
            st.write('[Learn more >](https://dimitardimitrov2001-visualisation-project-55-app-pmyr4y.streamlit.app/)')
        

        with right_column:
            st_lottie(lottie_coding, height=400, key='visualizations')




