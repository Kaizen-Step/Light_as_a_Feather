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
st.set_page_config(page_title='Aknowledgement - Light as a Feather',
                   page_icon=':bar_chart:', layout='wide')
st.title('🙏Aknowledgement')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Aknowledgement
st.write("""
We are grateful to all who helped us develop this project specially ****Mr. Ali Taslimi**** (twitter: @AliTslm ) with comprehensive streamlit open source project [Cross Chain Monitoring](https://github.com/alitslm/cross_chain_monitoring) that provides streamlit functions and tools. 
And also ****Flipside Crypto**** with massive database and last but not least ****MetricsDao**** that is the reason behind this project.
""")


# SQL Codes
st.write(""" ## SQL Codes ## """)

st.write("""
At the following links, you can find the SQL codes that are used in this dashboard: 

""")


st.write("""
1. https://app.flipsidecrypto.com/velocity/queries/188e0dd3-373f-4d47-ac41-32ae761e155f
2. https://app.flipsidecrypto.com/velocity/queries/c580b6d6-5b85-43da-914e-31c029159289
3. https://app.flipsidecrypto.com/velocity/queries/33200efd-330b-45ad-9d02-f09e7134412a
4. https://app.flipsidecrypto.com/velocity/queries/7d7b8187-29de-4deb-81db-ad139c5c6374
5. https://app.flipsidecrypto.com/velocity/queries/3e48917d-ad38-4892-91a8-5d321d9760c4
6. https://app.flipsidecrypto.com/velocity/queries/666ca8ad-c763-4831-b29e-f6c648324bbe
7. https://app.flipsidecrypto.com/velocity/queries/eb46f6ef-c7a6-49c5-868e-a7faaba8547e
8. https://app.flipsidecrypto.com/velocity/queries/a703f4b2-210f-48b3-abc2-c6c5f37bfaa8
9. https://app.flipsidecrypto.com/velocity/queries/d9346ec3-b6d2-45da-ba43-41b03afd888c
10. https://app.flipsidecrypto.com/velocity/queries/9dbae3b1-ab95-47e9-89bc-d26c6a01d9f8
11. https://app.flipsidecrypto.com/velocity/queries/195bf8df-3418-4365-8302-d0c61deb1216
12. https://app.flipsidecrypto.com/velocity/queries/328f1bda-dbbe-49ae-85a2-053c01333c7f
13. https://app.flipsidecrypto.com/velocity/queries/5f75bdd1-5010-427d-94a9-caed33fb610c
14. https://app.flipsidecrypto.com/velocity/queries/09c7e9ab-7aaa-4f58-869d-d0d34a078218
15. https://app.flipsidecrypto.com/velocity/queries/72c12f5a-72b2-4039-adc0-b43f52a80494
16. https://app.flipsidecrypto.com/velocity/queries/69325192-0e7b-4547-ab47-781c9552db37
17. https://app.flipsidecrypto.com/velocity/queries/6f303a26-78fe-4db1-b2a1-8a8149081293


""")
