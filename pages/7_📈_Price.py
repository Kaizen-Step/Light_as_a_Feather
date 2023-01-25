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
st.set_page_config(page_title='Price - Light As a Feather',
                   page_icon=':bar_chart:', layout='wide')
st.title('📈_Price')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Swaps':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/5f75bdd1-5010-427d-94a9-caed33fb610c/data/latest')
    elif query == 'Richest_users':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/60f07d44-b578-44ee-9cdb-7372b3029adf/data/latest')
    return None


Swaps = get_data('Swaps')
Richest_users = get_data('Richest_users')

st.subheader('Swap Daily Charts')

df = Swaps
df2 = Richest_users

# Daily Number of Swaps
fig = px.bar(df.sort_values(["DATE", "Daily Number of Swaps"], ascending=[
             True, False]), x="DATE", y="Daily Number of Swaps", color="STATUS", title='Daily Number of Swaps')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Number of Swaps")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Daily Number of Swapers
fig = px.bar(df.sort_values(["DATE", "Daily Number of Swappers"], ascending=[
             True, False]), x="DATE", y="Daily Number of Swappers", color="STATUS", title='Daily Number of Swapers')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Number of Swapers")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
