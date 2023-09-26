
import streamlit as st

st.markdown("# Perspective Data")
with st.container():
   image_col, text_col = st.columns((1,2))
   with image_col:
      st.image("./vsw_site.png")
   with text_col:
      st.markdown("## Senior consultancy in architecture, data and transformation")
st.markdown("### Vincent Swiderski - who am I?")
st.markdown("""
    Passionate about technology and data in particular, I love to help my customers tackling challenges at the crossroad of architecture and transformation with a strategic mindset.
    I learnt and care that humans are the key to sustainable achievements. Hence, I invest in understanding various stakeholders’ perspectives to onboard and co-deliver solid results.
    
    Evolving in industrial contexts since my early studies, I deeply believe in (and experienced) the concrete value that data can bring there.
    With 15+ years at Airbus, I acquired concrete skills that I am today further developing and leveraging with other industries.

    I am connected to a network of data professionals that I can leverage to address specific or bigger projects.

    I am the happy father of 2 wonderdul daughters, love connecting with nature, swimming, reading, chat with friends… and listening to data and technology podcasts 🤓
""")
st.markdown("### Typical missions")
st.markdown("""
Here are some of the typical missions I can help with, typically in lead or shadowing position:
- Data stack assessment, roadmap, business cases
- Data practice set-up or recovery
- Technical analysis for data driven use cases
- Architecture for data intensive applications
""")
st.markdown("### Experiences and projects")
st.markdown("""
- **Bombardier / Elevate Consulting (since mid 2022):** full time architecture consulting to set up and restructure the data landscape of Bombardier's customer applications team. Data team and practice set-up, data systems architecture review, data analytics engine selection.
- **NZTC / InDHu (since early 2022):** architecture and project advisory for the Offshore Energy Data Architecture project, aiming at proving benefits of data sharing mechanisms across UK offshore energy players, from Oil & Gas to Renewables.
- **Airbus**
    - **Skywise (2016 - 2021):** from early tiger team to deputy head of the Skywise project. Skywise is a significant data platform project as part of Airbus Digital Transformation, with 100+ industrial data driven application deployed, 150+ airlines integrated. 
    - **eSolutions and Smarter Fleet (2011 - 2015):** on-board the Airbus services digital journey starting from standalone Airbus developed solutions to a significant partnership with IBM.
- And some other undisclosable customers, in industrial contexts
""")
st.markdown("### Education")
st.markdown("""
- 2022: AWS Certified Solution Architect
- 2021: DSTI - Applied MSc in Data Science
- 2004: Supaero - Specialty in energetic systems and propulsion
- 2003: ECAM - MSc in industrial engineering
""")
st.markdown("### Contact")
st.markdown("""
Please feel free to reach me at vincent@perspectivedata.tech
""")