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
st.set_page_config(page_title='Transactions - Light as a Feather',
                   page_icon=':bar_chart:', layout='wide')
st.title('💸Transaction Metrics')

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


df = overview_Transactions1
df2 = overview_Transactions2
df3 = Luna_Tx_Volume

st.text(" \n")
st.write(""" ## Total TX""")


c1, c2 = st.columns(2)
with c1:
    st.write(""" #### Before Station Launched""")
    st.metric(label='**Total Transactions**',
              value=str(df2["Total Transactions"].map('{:,.0f}'.format).values[0]))

    st.metric(label='**Total Blocks**',
              value=df2["Total Blocks"].map('{:,.0f}'.format).values[0])

    st.metric(label='**Average Daily Transaction**',
              value=df2["Avg Daily Transactions"].map('{:,.0f}'.format).values[0])


with c2:
    st.write(""" #### After Station Launched """)
    st.metric(label='**Total Transactions**',
              value=str(df["Total Transactions"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Total Blocks**',
              value=df["Total Blocks"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Average Daily Transaction**',
              value=df["Avg Daily Transactions"].map('{:,.0f}'.format).values[0])

st.text(" \n")
st.write(""" Based on the charts, we can see that the number of transactions increased by 50 percent (from 81K to 118K) after the launch of the Station.  
There are an average of 18.9 K transactions per day, compared to 11.6 K daily transactions before the Station launch.There is also a significant difference in the number of users during these periods.  """)
st.text(" \n")


# Luna Daily Transactions
fig = px.bar(df3.sort_values(["DATE", "NUMBER_OF_TRANSACTIONS"], ascending=[
             True, False]), x="DATE", y="NUMBER_OF_TRANSACTIONS", color="STATUS", title='Luna Daily Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Daily Transactions")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.text(" \n")
c1, c2 = st.columns(2)

with c1:
    # Number of Transaction Pie chart
    fig = px.pie(df, values="Total Transactions",
                 names="STATUS", title='Number of Transaction Percentage Comparison', hole=0.5)
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+value', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    # Number of Transaction Pie chart
    fig = px.pie(df, values="Avg Daily Transactions",
                 names="STATUS", title='Average Daily Transaction Percentage Comparison', hole=0.5)
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+value', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.text(" \n")
st.text(" \n")

st.write(""" ## Transaction Fees """)

c1, c2 = st.columns(2)

with c1:
    st.write(" #### Before Station Launched")
    st.metric(label='**Total Fees[Luna]**',
              value=df2["Total Fees"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Max Transaction Fee[Luna]**',
              value=df2["MAX Fee"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Average Transaction Fee[Luna]**',
              value=df2["AVG Fee"].map('{:,.4f}'.format).values[0])
    st.metric(label='**Average Fee Per Block**',
              value=df2["Avg FEE per block"].map('{:,.0f}'.format).values[0])

with c2:
    st.write(" #### After Station Launched")
    st.metric(label='**Total Fees[Luna]**',
              value=df["Total Fees"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Max Transaction Fee[Luna]**',
              value=df["MAX Fee"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Average Transaction Fee[Luna]**',
              value=df["AVG Fee"].map('{:,.4f}'.format).values[0])
    st.metric(label='**Average Fee Per Block[Luna]**',
              value=df["Avg FEE per block"].map('{:,.0f}'.format).values[0])
st.text(" \n")

st.write(""" The total fee and average fee increase after the station launch which you can see the results in these charts. Another metrics that shows in the charts is average fee per block. As seen as in the chart this metrics also increased by 34 percent. Also, Compared to the previous chart, there has been an increase in the number of blocks. This has been seen with the number of blocks from 48.3 k reaching 56.8 k, which represents an increase of around 17 percent over the previous chart.  """)
st.text(" \n")


c1, c2 = st.columns(2)

with c1:
    # Number of Transaction Pie chart
    fig = px.pie(df, values="Total Fees",
                 names="STATUS", title='Total Fee Percentage Comparison', hole=0.5)
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+value', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


with c2:
    # Number of Transaction Pie chart
    fig = px.pie(df, values="AVG Fee",
                 names="STATUS", title='Average Transaction Fee Percentage', hole=0.5)
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+value', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.text(" \n")
# Luna Daily Volume
fig = px.bar(df3.sort_values(["DATE", "VOLUME"], ascending=[
             True, False]), x="DATE", y="VOLUME", color="STATUS", title='Luna Daily Volume')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Daily VOLUME")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.text(" \n")
st.write(""" ## Terra Users """)


c1, c2 = st.columns(2)
with c1:
    st.write(""" #### Before Station Launched """)

    st.metric(label='**Total Users**',
              value=df2["Total Users"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Aveage Daily Users**',
              value=df2["average Daily Users"].map('{:,.0f}'.format).values[0])


with c2:
    st.write(""" ####  After Station Launched""")
    st.metric(label='**Total Users**',
              value=df["Total Users"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Aveage Daily Users**',
              value=df["average Daily Users"].map('{:,.0f}'.format).values[0])

st.text(" \n")

st.write(""" There is also a significant difference in the number of users during these periods.Before the launch, there were 15.8K users, which shows a growth of around 40% compared to the 21K users afterward.There are an average of 3004 Users per day, compared to 2521 daily Users before the Station launch.
 """)


st.text(" \n")


c1, c2 = st.columns(2)

with c1:

   # Number of Transaction Pie chart
    fig = px.pie(df, values="Total Users",
                 names="STATUS", title='Total Users Percentage Comparison', hole=0.5)
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+value', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    # Number of Transaction Pie chart
    fig = px.pie(df, values="Total Blocks",
                 names="STATUS", title='Total Block Percentage Comparison', hole=0.5)
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+value', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
