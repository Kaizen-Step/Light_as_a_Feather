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
st.title('📈Price')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Price':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/33200efd-330b-45ad-9d02-f09e7134412a/data/latest')
    elif query == 'Richest_users':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/60f07d44-b578-44ee-9cdb-7372b3029adf/data/latest')
    return None


Price = get_data('Price')
Richest_users = get_data('Richest_users')

st.subheader('Luna Price Daily Charts')

st.write(""" Other than the Launch of Station, there are also other factors that contributed to the higher level of activity in the Terra blockchain, such as the recent market condition and growth in the price of Luna and Station was not the only reason behind price growth.
""")

df = Price
df2 = Richest_users

# Luna price
fig = px.area(df, x="DAY", y="PRICE",
              title='Luna price')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Price')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Luna price 2
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df["DAY"], y=df["PRICE"],
                      name="PRICE"),  secondary_y=True)
fig.update_layout(
    title_text='Luna Price change')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Price')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
