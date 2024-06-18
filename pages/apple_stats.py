import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import mplfinance as mpf
import warnings
warnings.filterwarnings('ignore')

st.title('Information about Appple stocks')

def japanese_candle_function(ticker, period):
    df = yf.download(ticker, period=period)
    if df.empty:
        st.write("Please check the ticker symbol and try again.")
    else:
        st.write(df.head())
        
        st.subheader(f'Japanese candle graph for {period}')
        
        df.reset_index(inplace=True)
        df.set_index('Date', inplace=True)
        
        fig, ax = mpf.plot(df, type='candle', style='charles',figsize=(12, 8), volume=True, returnfig=True)
        fig.savefig('japanesecandle.png')
        
        st.image('japanesecandle.png')
        
        with open('japanesecandle.png', 'rb') as file:
                btn = st.download_button(
                    label='Download PNG file',
                    data=file,
                    file_name='japanesecandle.png',
                    mime='image/png'
                )
                
if st.sidebar.button('1 Day'):
    japanese_candle_function('AAPL', '1d')
if st.sidebar.button('1 Week (5 work days)'):
    japanese_candle_function('AAPL', '5d')
if st.sidebar.button('1 Month'):
    japanese_candle_function('AAPL', '1mo')
if st.sidebar.button('1 Year'):
    japanese_candle_function('AAPL', '1y') 
