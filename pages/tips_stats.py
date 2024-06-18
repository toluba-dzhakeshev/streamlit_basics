import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

st.title('Some interesting graphs describing Tips dataframe')

uploaded_file = st.sidebar.file_uploader('Upload CSV file', type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(5))
    
    if st.sidebar.button('Tips dinamic over time'):
        st.subheader('Tips dinamic over time')    
        graph1 = sns.displot(data=df, x='tip', col='time', kde=True)
        graph1.fig.savefig('tips_dynamic_over_time.png', dpi=300)
        st.image('tips_dynamic_over_time.png')
        
        with open('tips_dynamic_over_time.png', 'rb') as file:
                btn = st.download_button(
                    label='Download PNG file',
                    data=file,
                    file_name='tips_dynamic_over_time.png',
                    mime='image/png'
                )
    
    if st.sidebar.button('Total bill'):
        st.subheader('Total bill')
        fig, ax = plt.subplots()
        graph2 = sns.histplot(data=df, x='total_bill', ax=ax)
        fig.savefig('total_bill_distribution.png', dpi=300)
        st.image('total_bill_distribution.png')
        
        with open('total_bill_distribution.png', 'rb') as file:
                btn = st.download_button(
                    label='Download PNG file',
                    data=file,
                    file_name='total_bill_distribution.png',
                    mime='image/png'
                )
    
    if st.sidebar.button('Total bill for each day'):
        st.subheader('Total bill for each day')
        fig2, ax2 = plt.subplots()
        graph3 = sns.boxplot(data=df, x='total_bill', y='day', hue='time', ax=ax2)
        fig2.savefig('total_bill_each_day.png', dpi=300)
        st.image('total_bill_each_day.png')
        
        with open('total_bill_each_day.png', 'rb') as file:
                btn = st.download_button(
                    label='Download PNG file',
                    data=file,
                    file_name='total_bill_each_day.png',
                    mime='image/png'
                )
    
else:
    st.stop()
    