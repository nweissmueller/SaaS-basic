import streamlit as st
from st_paywall import add_auth

st.set_page_config(layout="wide")
st.title("Basic Saas :rocket:")

# pay and subscription wall
add_auth(required=True)

# view subsequent code requires authentication + subscription
st.write(f"Subscription Status: {st.session_state.user_subscribed}")
st.write(f"Your email {st.session_state.email} is subscribed!")
st.write("Yay! :partying_face: You're good to go.")
