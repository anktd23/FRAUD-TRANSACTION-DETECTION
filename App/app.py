import streamlit as st
from dataset_module import dict_retrieve
from stats_mod import avg_trans,avg_trans_all,mode_trans,mode_trans_all,median_trans,median_trans_all,iqr_trans,iqr_trans_all,centroid,std_dev,fraudulent_trans
import sys
from utils import median,mean,dict_retrieve_,standard_dev,iqr
file = 'Transaction.txt'
data = dict_retrieve(file)

st.set_page_config(layout='wide',page_title='Statistics Calculator')
st.sidebar.header("Statistics Calculator")

col1, col2, col3 = st.columns(3)
user = st.sidebar.radio('Select users',['Single user','All users'])
if user == 'Single user':
    users = st.sidebar.selectbox('Select user id',[21,22,23,24,25,26,27,28,29,30])
    user = str(users)
    with col1:
        st.header("Mean")
        st.text(avg_trans(data,user))
        st.header("IQR")
        st.text(iqr_trans(data,user))
    with col2:
        st.header("Mode")
        st.text(mode_trans(data,user))
        st.header("Centroid") 
        st.text(centroid(data,user))
    with col3:
        st.header("Median")
        st.text(median_trans(data,user))      
        st.header("Std Dev")
        st.text(std_dev(data,user))
        
else:
    with col1:
        st.header('Mean')
        st.text(avg_trans_all(data))
        st.header("IQR")
        st.text(iqr_trans_all(data))
    with col2:
        st.header("Mode")
        st.text(mode_trans_all(data))
    with col3:
        st.header("Median")
        st.text(median_trans_all(data)) 

transaction = []
for key in dict_retrieve_(file):
    transaction.append(key)
transaction_id = st.sidebar.selectbox('Enter the transaction id',transaction)
transaction = str(transaction_id)
with col1:
    st.header('Fraudulent Transaction')
    st.text(fraudulent_trans(file,transaction))





