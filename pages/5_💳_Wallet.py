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
st.set_page_config(page_title='Wallets - Light as a Feather',
                   page_icon=':bar_chart:', layout='wide')
st.title('💳Wallets')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'TerraStation_New_Active_Wallets':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/c580b6d6-5b85-43da-914e-31c029159289/data/latest')
    elif query == 'Terra_Staion_Wallets':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/188e0dd3-373f-4d47-ac41-32ae761e155f/data/latest')
    return None


TerraStation_New_Active_Wallets = get_data('TerraStation_New_Active_Wallets')
Terra_Staion_Wallets = get_data('Terra_Staion_Wallets')

st.subheader('Wallet Charts')

df = TerraStation_New_Active_Wallets
df2 = Terra_Staion_Wallets

st.write(""" According to the charts, active wallets have increased significantly since Station launched.
There are 42K active wallets on 15 Jan, almost twice as many as on 9 Jan, which was the highest number for the days leading up to launch (22K).Also, new wallets are increased after the Station launch. """)


# Daily Number of New Wallets
fig = px.bar(df.sort_values(["DATE", "NEW_WALLETS"], ascending=[
             True, False]), x="DATE", y="NEW_WALLETS", color="STATUS", title='Daily Number of New Wallets')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Number of New Wallets")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Daily Number of Active Wallets
fig = px.bar(df2.sort_values(["DATE", "ACTIVE_WALLETS"], ascending=[
             True, False]), x="DATE", y="ACTIVE_WALLETS", color="STATUS", title='Daily Number of Active Wallets')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Number of Active Wallets")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
