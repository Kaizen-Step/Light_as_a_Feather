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
st.set_page_config(page_title='Swaps - Light as a Feather',
                   page_icon=':bar_chart:', layout='wide')
st.title('🌌Swap Metrics')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Swaps':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/5f75bdd1-5010-427d-94a9-caed33fb610c/data/latest')
    elif query == 'Terra_Swaps':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/07295a8d-e2c3-4f5e-9e05-a722237b6af2/data/latest')
    return None


Swaps = get_data('Swaps')
Terra_Swaps = get_data('Terra_Swaps')


st.text(" \n")
st.write(""" ### Daily Swaps""")
st.write('Terra has seen a significant increase in the number of swaps since Station launched, as you can see in the following charts. The number of swaps Tripled on January 14 with 5059 daily swaps and kept rising until it hit a weekly peak of 6171 on January 15, but Station impact did not last more than three days, and at the end of the week, the daily number came back to 1364 which quite alike the day before Station Launched.  ')

df = Swaps
df2 = Terra_Swaps

# Daily Number of Swaps
fig = px.bar(df.sort_values(["DATE", "Daily Number of Swaps"], ascending=[
             True, False]), x="DATE", y="Daily Number of Swaps", color="STATUS", title='Daily Number of Swaps')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Number of Swaps")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.text(" \n")
st.write(""" ### Daily Swapers""")
st.write('The number of swapers increased after announcment, but compared to number of swaps, this increase was not significant as the number of swapers on jan 14 increased by 97 in a day not multipled, and reached the peak of 407 on jan 15.  ')
# Daily Number of Swapers
fig = px.bar(df.sort_values(["DATE", "Daily Number of Swappers"], ascending=[
             True, False]), x="DATE", y="Daily Number of Swappers", color="STATUS", title='Daily Number of Swapers')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Number of Swapers")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.text(" \n")
st.write(""" ### Daily Swap Volume to Luna & From Luna""")
st.write('The daily swap volume to Luna was higher before the station announcment and with 261M 2 days before station launched made a record. while, ater station launched there was no hype on swaping to Luna and with 19M high on jan 15  and 383k low on jan 20 showed a regular week.  ')

# daily Volume of Luna Swaps[Swaps to Luna]
fig = px.bar(df2.sort_values(["DATE", "VOLUME2"], ascending=[
             True, False]), x="DATE", y="VOLUME2", color="STATUS", title='Daily Volume of Luna Swaps[to Luna]')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Daily Volume")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# daily Volume of Luna Swaps[Swaps to Luna]
fig = px.bar(df2.sort_values(["DATE", "VOLUME1"], ascending=[
             True, False]), x="DATE", y="VOLUME1", color="STATUS", title='Daily Volume of Luna Swaps[From Luna]')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Daily Volume")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Total volume of Luna swaps
fig = px.bar(df2.sort_values(["DATE", "VOLUME"], ascending=[
             True, False]), x="DATE", y="VOLUME", color="STATUS", title='Total volume of Luna swaps')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Daily Volume")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
