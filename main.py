import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

st.title('Data analysis application')

uploaded_file = st.sidebar.file_uploader('Upload CSV file', type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(5))
else:
    st.stop()
    
missing_values = df.isna().sum()
missing_values = missing_values[missing_values > 0]
# st.write(missing_values)
if len(missing_values) > 0:
    fig, ax = plt.subplots()
    sns.barplot(x=missing_values.index, y=missing_values.values)
    ax.set_title('Missing values in columns')
    st.pyplot(fig)
    
    button = st.button('Fill in missing values')
    if button:
        df_filled = df[missing_values.index].copy()
        # st.write(df_filled)

        for col in df_filled.columns:
            if df_filled[col].dtype == 'object':
                df_filled[col] = df_filled[col].fillna(df_filled[col].mode()[0])
            else:
                df_filled[col] = df_filled[col].fillna(df_filled[col].median())
                
        # st.write(df_filled.head(5))

        download_button = st.download_button(label='Download CSV file',
                   data=df_filled.to_csv(),
                   file_name='filled_file.csv')
        
else:
    st.write('There are no missing values')
    st.stop()
