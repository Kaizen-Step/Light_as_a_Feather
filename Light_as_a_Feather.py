# Libraries
import streamlit as st
from PIL import Image


# Layout
st.set_page_config(page_title='Light As a Feather',
                   page_icon=':bar_chart:', layout='wide')
st.title('Light as a Feather')

# Content
c1, c2, c3, c4 = st.columns(4)
c4.image(Image.open('Images/3.png'))
with c1:
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")

    st.write("""# 🌔Terra (Station) #""")

st.write("""
Terra is a blockchain protocol and payment platform used for algorithmic stablecoins. The project was created in 2018 by Terraform Labs, a startup co-founded by Do Kwon and Daniel Shin. It is most known for its Terra stablecoin and the associated Luna reserve asset cryptocurrency.  
In May 2022, the Terra blockchain was temporarily halted after the collapse of the stablecoin TerraUSD (UST) and Luna, in an event that wiped out almost USD45 billion in capitalization within a week. 

### What is Terra Station ? ###
Terra Station is the official mobile wallet for managing native Terra assets and tokens. and connecting with decentralized applications running on the Terra blockchain. Main Features: - Non-custodial wallet application (you control your keys) - Create a new Terra wallet or recover from seed phrase.  
Each blockchain has its own specific wallet. The Terra Network is picking up the pieces after the Luna/UST crash. Terra Station is the official wallet for the Terra network and blockchain. As such, it’s capable of handling all native Terra assets and tokens. It’s available as a mobile app, on both Android and iOS. Furthermore, there’s also a desktop version available. 
Terra has easy-to-follow instructions on how you can install the mobile app or the desktop version.it has many functionalities. For instance: Swap, Stake, Governance, NFTs.
 
### Is Terra Station Decentralized? ###
In theory, the Terra Station is a decentralized wallet. In any case, it’s a non-custodial wallet. This means that you oversee the wallet. You are the only one who has access to the private keys.
After the downfall of the LUNA/UST tokens, the Terra Network had a rough time. Out of the 73 projects building on the Terra Network in March 2022, 48 left for Polygon.
There are also views that the platform was not decentralized. Analytics Insights makes a case for this, blaming Do Kwon’s ownership of LUNA tokens. On the other hand, this should not affect the Terra Station. The reason being, as already mentioned, is that you are in control of the wallet. 
### What Network Does Terra Station Use? ###
Terra Station uses the Terra network. It’s the native wallet for the network and of the Terra blockchain. Terra was built in the Cosmos network. As a result, it uses the Tendermint Delegated-Proof-of-Stake (DPoS) as its consensus mechanism.
It’s also part of the ICB. That’s the Inter-Blockchain Communication protocol of Cosmos. This allows all blockchains inside the ICB to talk to each other.
However, the current Terra network is rather small. We mentioned already that 47 projects are left for Polygon. The remaining projects are still due two LUNA airdrops, so they can keep building. One is due on September 17th, 2022. This airdrop covers 35 projects.


### Methodology ###

The Terra community announced the launch of the Station on 14 January. This announcement has generated hype in the Terra community. Has this hype translated to an increase in activity ?  
To answer this question The Terra core schema tables on the Flipside database are used to obtain the necessary data.
It was taken into account the period 7 days before the  announcement and 7 days after the  announcement (07 Jan-21 Jan).
Metrics are show in 5 category:  
1- overview: include a summary of the overall metrics before and after the Station Lunch.  
2- Governance: include Staking Luna metrics before and after the Station Lunch.  
3- Transactions and Swaps: include metrics about Luna swaps and transactions before and after the Station Lunch.  
4- Bridge: include metrics about bridge transactions before and after the Station Lunch.   
5- Price: review price change before and after this announcement.

This dashboard uses the following tables:   
* terra.core.fact_transactions
* terra.core.ez_staking
* terra.core.ez_swaps



 
 """
         )


st.write("""   
### Sources    """)
st.write("""    1.https://www.altcoinbuzz.io/reviews/4-questions-about-terra-station-part-1/  
        2.https://www.bloomberg.com/news/articles/2022-05-14    
        3.https://social.techcrunch.com/2022/05/12/    
        4.https://www.blockchaines.tech/en/guide/how-terra-station-works/
              """)
c1, c2 = st.columns(2)
with c2:
    st.info(
        '**Project Supervisor:  [MetricsDao](https://metricsdao.notion.site/)**', icon="👨🏻‍💼")
    st.info(
        '**Project GuitHub:  [Light as a Feather](https://github.com/Kaizen-Step/Light_as_a_Feather)**', icon="💻")
with c1:
    st.info(
        '**Data:  [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="🧠")
    st.info(
        '**Twitter:  [Ludvig.1989](https://flipsidecrypto.xyz/)**', icon="🦜")
