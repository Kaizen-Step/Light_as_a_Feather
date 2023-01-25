# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Transactions - Light As a Feather',
                   page_icon=':bar_chart:', layout='wide')
st.title('💸Transactions')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'overview_Transactions1':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/69325192-0e7b-4547-ab47-781c9552db37/data/latest')
    elif query == 'overview_Transactions2':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/72c12f5a-72b2-4039-adc0-b43f52a80494/data/latest')
    elif query == 'Luna_Tx_Volume':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/09c7e9ab-7aaa-4f58-869d-d0d34a078218/data/latest')
    return None


overview_Transactions1 = get_data('overview_Transactions1')
overview_Transactions2 = get_data('overview_Transactions2')
Luna_Tx_Volume = get_data('Luna_Tx_Volume')


st.subheader('Overview')
df = overview_Transactions1
df2 = overview_Transactions2
df3 = Luna_Tx_Volume


c1, c2 = st.columns(2)
with c1:
    st.write(""" #### Before Station Launched """)
    st.metric(label='**Total Transactions**',
              value=str(df2["Total Transactions"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Total Fees**',
              value=df2["Total Fees"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Max Transaction Fee**',
              value=df2["MAX Fee"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Average Transaction Fee**',
              value=df2["AVG Fee"].map('{:,.2f}'.format).values[0])
    st.metric(label='**Total Blocks**',
              value=df2["Total Blocks"].map('{:,.4f}'.format).values[0])
    st.metric(label='**Average Fee Per Block**',
              value=df2["Avg FEE per block"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Average Daily Transaction**',
              value=df2["Avg Daily Transactions"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Total Users**',
              value=df2["Total Users"].map('{:,.2f}'.format).values[0])
    st.metric(label='**Aveage Daily Users**',
              value=df2["average Daily Users"].map('{:,.4f}'.format).values[0])
with c2:
    st.write(""" #### After Station Launched """)
    st.metric(label='**Total Transactions**',
              value=str(df["Total Transactions"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Total Fees**',
              value=df["Total Fees"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Max Transaction Fee**',
              value=df["MAX Fee"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Average Transaction Fee**',
              value=df["AVG Fee"].map('{:,.2f}'.format).values[0])
    st.metric(label='**Total Blocks**',
              value=df["Total Blocks"].map('{:,.4f}'.format).values[0])
    st.metric(label='**Average Fee Per Block**',
              value=df["Avg FEE per block"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Average Daily Transaction**',
              value=df["Avg Daily Transactions"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Total Users**',
              value=df["Total Users"].map('{:,.2f}'.format).values[0])
    st.metric(label='**Aveage Daily Users**',
              value=df["average Daily Users"].map('{:,.4f}'.format).values[0])

st.text(" \n")
st.text(" \n")
st.write(""" ### Luna Daily Metrics   """)
st.text(" \n")
st.text(" \n")

# Luna Daily Volume
fig = px.bar(df3.sort_values(["DATE", "VOLUME"], ascending=[
             True, False]), x="DATE", y="VOLUME", color="STATUS", title='Luna Daily Volume')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Daily VOLUME")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Luna Daily Transactions
fig = px.bar(df3.sort_values(["DATE", "NUMBER_OF_TRANSACTIONS"], ascending=[
             True, False]), x="DATE", y="NUMBER_OF_TRANSACTIONS", color="STATUS", title='Luna Daily Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Daily Transactions")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
