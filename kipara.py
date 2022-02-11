#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
st.header=("TEMPERATUR IN FAHRENHEIT")
c=st.number_input("what is temperatur")
st.write("fahrenheit is" ,c*9/5+32) 

