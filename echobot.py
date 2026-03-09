import streamlit as st 
import numpy as np 

with st.chat_message("assistant"):
    st.write("Hello human")
    st.bar_chart(np.random.rand(30,3))
