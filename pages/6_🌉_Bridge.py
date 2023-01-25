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
st.set_page_config(page_title='Bridge - Light As a Feather',
                   page_icon=':bar_chart:', layout='wide')
st.title('🌉Bridge')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'bridge_out_overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/328f1bda-dbbe-49ae-85a2-053c01333c7f/data/latest')
    elif query == 'bridge_out_overview2':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/195bf8df-3418-4365-8302-d0c61deb1216/data/latest')
    elif query == 'bridgedout_TX':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/9dbae3b1-ab95-47e9-89bc-d26c6a01d9f8/data/latest')
    elif query == 'bridgedout_User':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/d9346ec3-b6d2-45da-ba43-41b03afd888c/data/latest')
    elif query == 'bridge_out_daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a703f4b2-210f-48b3-abc2-c6c5f37bfaa8/data/latest')
    return None


bridge_out_overview = get_data('bridge_out_overview')
bridge_out_overview2 = get_data('bridge_out_overview2')
bridgedout_TX = get_data('bridgedout_TX')
bridgedout_User = get_data('bridgedout_User')
bridge_out_daily = get_data('bridge_out_daily')

st.subheader('Overview')
df = bridge_out_overview
df2 = bridge_out_overview2
df3 = bridgedout_TX
df4 = bridgedout_User
df5 = bridge_out_daily

c1, c2 = st.columns(2)
with c1:
    st.write(""" #### Before Station Launched """)
    st.metric(label='**Active Users**',
              value=str(df2["ACTIVE_USERS"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Volume**',
              value=df2["VOLUME"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Number**',
              value=df2["NUMBER"].map('{:,.0f}'.format).values[0])

with c2:
    st.write(""" #### After Station Launched """)
    st.metric(label='**Active Users**',
              value=str(df["ACTIVE_USERS"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Volume**',
              value=df["VOLUME"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Number**',
              value=df["NUMBER"].map('{:,.0f}'.format).values[0])


st.text(" \n")
st.text(" \n")
st.write(""" ### Bridge Metrics   """)
st.text(" \n")
st.text(" \n")

# Bridged Out - Number of Transactions
fig = px.pie(df, values="NUMBER",
             names="STATUS", title='Bridged Out - Number of Transactions', hole=0.5)
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Bridged Out - Number of Volume
fig = px.pie(df, values="VOLUME",
             names="STATUS", title='Bridged Out - Volume', hole=0.5)
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Bridged Out - Number of Users
fig = px.pie(df, values="ACTIVE_USERS",
             names="STATUS", title='Bridged Out - Number of Active User', hole=0.5)
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write(""" ### Bridge out Range Distribution """)

# Distribution of transactions based on "bridged out" Number of Bridge
fig = px.bar(df3.sort_values(["BRIDGE_RANGE", "NUMBER_OF_BRIDGES"], ascending=[
             True, False]), x="BRIDGE_RANGE", y="NUMBER_OF_BRIDGES", color="STATUS", title='Distribution of transactions based on "bridged out" Number of Bridge')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Number of Bridge")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Distribution of transactions based on "bridged out" Number of Users
fig = px.bar(df4.sort_values(["BRIDGE_RANGE", "NUMBER_OF_USERS"], ascending=[
             True, False]), x="BRIDGE_RANGE", y="NUMBER_OF_USERS", color="STATUS", title='Distribution of transactions based on "bridged out" Number of Users')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Number of Users")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" ### Daily Bridge out  """)

# Daily bridged out volume
fig = px.bar(df5.sort_values(["DATE", "VOLUME"], ascending=[
             True, False]), x="DATE", y="VOLUME", color="STATUS", title=' Daily bridged out Volume')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Volume")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Daily bridged out Users
fig = px.bar(df5.sort_values(["DATE", "ACTIVE_USERS"], ascending=[
             True, False]), x="DATE", y="ACTIVE_USERS", color="STATUS", title=' Daily bridged out Users')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="ACTIVE_USERS")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


##############################################
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
