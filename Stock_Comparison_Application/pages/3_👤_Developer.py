import streamlit as st

# Set page configuration
st.set_page_config(page_title="Developer Information", page_icon="👨‍💻", layout="wide")

# Developer information
developer_info = {
    "Name": "Dharani Ilango",
    "Role": "Designer and Analyst",
    "Portfolio": "https://idharani.netlify.app",
    "LinkedIn": "https://www.linkedin.com/in/dharaniilango1209/",
    "Instagram": "https://www.instagram.com/dharani___1209/",
    "Email": "dharaniilango1209@gmail.com",
    "GitHub": "https://github.com/dharaniilango",
}

# Page Title
st.title("👨‍💻 Developer Information")

# Section for developer's profile
st.markdown("## About the Developer")
st.write(" ")

# Basic Information with Icons
st.subheader("Contact Information")
st.write(" ")

# Create columns for layout
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Name:** " + developer_info["Name"])
    st.markdown("**Role:** " + developer_info["Role"])

with col2:
    st.markdown("**Email:** [" + developer_info["Email"] + "](mailto:" + developer_info["Email"] + ")")
    
with col3:
    st.markdown("**Portfolio:** [Website](" + developer_info["Portfolio"] + ")")

st.write(" ")
# Create another row of columns for social links
st.subheader("Social Links")

# Create columns for layout
col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("**LinkedIn:** [Dharani-Ilango](" + developer_info["LinkedIn"] + ")")
with col5:
    st.markdown("**Instagram:** [dharani___1209](" + developer_info["Instagram"] + ")")
with col6:
    st.markdown("**GitHub:** [DharaniIlango](" + developer_info["GitHub"] + ")")

st.write(" ")
# Footer
st.header("Connect with Me!")
st.markdown(
    """
    Feel free to reach out for project collaborations, inquiries, or just a chat!
    """
)