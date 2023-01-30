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
st.set_page_config(page_title='Supply - Light As a Feather',
                   page_icon=':bar_chart:', layout='wide')
st.title('🏛️Governance')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'weekly_staking_action':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/eb46f6ef-c7a6-49c5-868e-a7faaba8547e/data/latest')
    elif query == 'Daily_staking_Reward':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/666ca8ad-c763-4831-b29e-f6c648324bbe/data/latest')
    elif query == 'Daily_Unstaking_Actions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3e48917d-ad38-4892-91a8-5d321d9760c4/data/latest')
    elif query == 'Daily_net_staking_actions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/7d7b8187-29de-4deb-81db-ad139c5c6374/data/latest')
    elif query == 'Reward_Recievers':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/7cff5cc4-779c-4637-81f4-5716a0f76eee/data/latest')
    return None


weekly_staking_action = get_data('weekly_staking_action')
Daily_staking_Reward = get_data('Daily_staking_Reward')
Daily_Unstaking_Actions = get_data('Daily_Unstaking_Actions')
Daily_net_staking_actions = get_data('Daily_net_staking_actions')
Reward_Recievers = get_data('Reward_Recievers')


df = weekly_staking_action
df2 = Daily_staking_Reward
df3 = Daily_Unstaking_Actions
df4 = Daily_net_staking_actions
df5 = Reward_Recievers


st.write(""" ### Daily Staking Actions """)
# Number of Delegators
fig = px.bar(df.sort_values(["DATE", "WALLET"], ascending=[
             True, False]), x="DATE", y="WALLET", color="STATUS", title='Number of Delegators ')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Number of Delagators")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Daily staking actions-Volume
fig = px.bar(df.sort_values(["DATE", "VOLUME"], ascending=[
             True, False]), x="DATE", y="VOLUME", color="STATUS", title='Daily staking actions-Volume')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Staking Action Volume")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Daily Staking Transactions
fig = px.bar(df.sort_values(["DATE", "NUMBER_OF_TX"], ascending=[
             True, False]), x="DATE", y="NUMBER_OF_TX", color="STATUS", title='Daily Staking Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Daily Number of Transactions")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" ### Daily Staking Rewards """)

# staking reward- usd scale
fig = px.bar(df2.sort_values(["DATE", "STAKING_REWARDS_USD"], ascending=[
             True, False]), x="DATE", y="STAKING_REWARDS_USD", color="STATUS", title='Staking Reward-[USD]')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Staking Reward [USD]")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write(""" ### Daily Unstaking Actions """)

# Number of UnDelegators
fig = px.bar(df3.sort_values(["DATE", "WALLET"], ascending=[
             True, False]), x="DATE", y="WALLET", color="STATUS", title='Number of Undelegators ')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Number of Undelagators")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Daily Unstaking actions-Volume
fig = px.bar(df3.sort_values(["DATE", "VOLUME"], ascending=[
             True, False]), x="DATE", y="VOLUME", color="STATUS", title='Daily Unstaking actions-Volume')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Unstaking Action Volume")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Daily Unstaking Transactions
fig = px.bar(df3.sort_values(["DATE", "NUMBER"], ascending=[
             True, False]), x="DATE", y="NUMBER", color="STATUS", title='Daily Unstaking Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Daily Number of Transactions")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" ### Daily Net Staking Actions """)

# Daily Net volume Staking
fig = px.bar(df4.sort_values(["DATE", "NET Volume"], ascending=[
             True, False]), x="DATE", y="NET Volume", color="STATUS", title='Daily Net volume Staking')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="NET Volume")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


##########################################
