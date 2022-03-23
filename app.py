import streamlit as st
import pandas as pd

st.markdown('''# **Binance Price App**
A simple cryptocurrency price app pulling price data from *Binance API*.
''')

st.header('**Selected Price**')

# Load market data from Binance API..
df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

def round_val(value):
    if value.values > 1:
        temp = float(round(value, 2))
    else:
        temp = float(round(value, 8))
    return temp

column1, column2, column3 = st.columns(3)

# Widget (Cryptocurrency selection box)..
select_col1 = st.sidebar.selectbox('Price 1', df.symbol, list(df.symbol).index('BTCBUSD'))
select_col2 = st.sidebar.selectbox('Price 2', df.symbol, list(df.symbol).index('ETHBUSD'))
select_col3 = st.sidebar.selectbox('Price 3', df.symbol, list(df.symbol).index('BNBBUSD'))
select_col4 = st.sidebar.selectbox('Price 4', df.symbol, list(df.symbol).index('XRPBUSD'))
select_col5 = st.sidebar.selectbox('Price 5', df.symbol, list(df.symbol).index('ADABUSD'))
select_col6 = st.sidebar.selectbox('Price 6', df.symbol, list(df.symbol).index('DOGEBUSD'))

# DataFrame of selected Cryptocurrency..
df_col1 = df[df.symbol == select_col1]
df_col2 = df[df.symbol == select_col2]
df_col3 = df[df.symbol == select_col3]
df_col4 = df[df.symbol == select_col4]
df_col5 = df[df.symbol == select_col5]
df_col6 = df[df.symbol == select_col6]

# Apply a custom function to conditionally round values..
price_col1 = round_val(df_col1.weightedAvgPrice)
price_col2 = round_val(df_col2.weightedAvgPrice)
price_col3 = round_val(df_col3.weightedAvgPrice)
price_col4 = round_val(df_col4.weightedAvgPrice)
price_col5 = round_val(df_col5.weightedAvgPrice)
price_col6 = round_val(df_col6.weightedAvgPrice)

# Select the priceChangePercent column..
percent_col1 = f'{float(df_col1.priceChangePercent)}%'
percent_col2 = f'{float(df_col2.priceChangePercent)}%'
percent_col3 = f'{float(df_col3.priceChangePercent)}%'
percent_col4 = f'{float(df_col4.priceChangePercent)}%'
percent_col5 = f'{float(df_col5.priceChangePercent)}%'
percent_col6 = f'{float(df_col6.priceChangePercent)}%'

# Create a metrics price box..
column1.metric(select_col1, price_col1, percent_col1)
column2.metric(select_col2, price_col2, percent_col2)
column3.metric(select_col3, price_col3, percent_col3)
column1.metric(select_col4, price_col4, percent_col4)
column2.metric(select_col5, price_col5, percent_col5)
column3.metric(select_col6, price_col6, percent_col6)

st.header('**All Price**')
st.dataframe(df)

st.info('Created by Mohammad Kumail (https://github.com/kumail11') 
st.info('Youtube Channel: (https://www.youtube.com/channel/UCQhtFIRoBy_Ai6YrXXd-fjQ)')