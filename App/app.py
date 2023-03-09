import streamlit as st
from dataset_mod import dict_retrieve
from dist_mod import euclidean_dist_same,euclidean_dist_diff,euclidean_distance
from stats_mod import avg_trans,avg_trans_all,mode_trans,mode_trans_all,median_trans,median_trans_all,iqr_trans,iqr_trans_all,centroid,std_dev,fraudulent_trans,abnormal_trans,zscore,zscore_all,freq_tran_loc,outlier_det,nth_percentile,nth_percentile_all
from utils import dict_retrieve_
file = 'Transaction.txt'
data = dict_retrieve(file)

st.set_page_config(layout="wide",page_title='Statistics Calculator')
st.sidebar.header("Statistics Calculator")
selection = st.sidebar.radio('Select one',['Euclidean distance','Statistics'])
if selection =='Euclidean distance':
    transaction = []
    for key in dict_retrieve_(file):
        transaction.append(key)
    selection = st.sidebar.radio('Select one',['Same user','Different user'])
    if selection == 'Same user':
        users = st.sidebar.selectbox('Select user id',[21,22,23,24,25,26,27,28,29,30])
        user = str(users)
        transaction_id1 = st.sidebar.selectbox('Enter the transaction id1',transaction)
        transaction_id2 = st.sidebar.selectbox('Enter the transaction id2',transaction)
        st.subheader("Euclidean distance between two transaction for same user.")
        st.text(euclidean_dist_same(data,user,transaction_id1,transaction_id2))
    else:
        users = st.sidebar.selectbox('Select user id 1',[21,22,23,24,25,26,27,28,29,30])
        user1 = str(users)
        transaction_id1 = st.sidebar.selectbox('Enter the transaction for user 1',transaction)
        users = st.sidebar.selectbox('Select user id 2',[21,22,23,24,25,26,27,28,29,30])
        user2 = str(users)
        transaction_id2 = st.sidebar.selectbox('Enter the transaction user 2',transaction)
        st.subheader("Euclidean distance between two transaction for different user.")
        st.text(euclidean_dist_diff(data,user1,user2,transaction_id1,transaction_id2))

else:
    col1, col2, col3,col4 = st.columns(4)
    user = st.sidebar.radio('Select users',['Single user','All users'])

    if user == 'Single user':
        users = st.sidebar.selectbox('Select user id',[21,22,23,24,25,26,27,28,29,30])
        user = str(users)
        x_cord = st.sidebar.text_input("Enter x co-ordinates")
        y_cord = st.sidebar.text_input("Enter y co-ordinates")
        percentile = st.sidebar.text_input("Enter nth percentile")
        transaction = []
        for key in dict_retrieve_(file):
            transaction.append(key)
        transaction_id = st.sidebar.selectbox('Enter the transaction id',transaction)
        transaction = str(transaction_id)
        with col1:
            st.subheader("Mean")
            st.text(avg_trans(data,user))
            st.subheader("Mode")
            st.text(mode_trans(data,user)) 
            st.subheader("Centroid") 
            st.text(centroid(data,user))

        with col2:
            st.subheader("Median")
            st.text(median_trans(data,user)) 
            st.subheader("Abn Trans")
            st.text(abnormal_trans(data,user))
            st.subheader('Trans Freq')
            st.text(freq_tran_loc(data,x_cord,y_cord))

        with col3:
            st.subheader("IQR")
            st.text(iqr_trans(data,user))
            st.subheader("Z Score")
            st.text(zscore(data,user)) 
            st.subheader('Fraud Tran')
            st.text(fraudulent_trans(file,transaction)) 

        with col4:
            st.subheader("Std Dev")
            st.text(std_dev(data,user))
            st.subheader("Nth percentile")
            st.text(nth_percentile(data,user,percentile))
            st.subheader("Outlier")
            st.text(outlier_det(data,user,x_cord,y_cord)) 
            
    else:
        percentile = st.sidebar.text_input("Enter nth percentile")
        with col1:
            st.subheader('Mean')
            st.text(avg_trans_all(data))
            st.subheader('Z Score')
            st.text(zscore_all(data))
        with col2:
            st.subheader("Mode")
            st.text(mode_trans_all(data))
            st.subheader("Nth percentile")
            st.text(nth_percentile_all(data,percentile))
        with col3:
            st.subheader("Median")
            st.text(median_trans_all(data)) 
        with col4:
            st.subheader("IQR")
            st.text(iqr_trans_all(data))








