import streamlit as st

st.set_page_config(page_title="Talladega Testing")

# Initialize session state variables
if "click_count" not in st.session_state:
    st.session_state.click_count = 0

# Define what to show based on click count
if st.session_state.click_count == 0:
    label_text = "Gentlemen...Ensure your flash is ready!!!"
    button_text = "Click here for boobies!!!"
elif st.session_state.click_count == 1:
    label_text = "( • )( • )    ( • )( • )    ( • )( • )    ( • )( • )"
    button_text = "Ha!  Got Yo Ass!"
else:
    st.success("Session Ended. Bye!")
    st.stop()

# Display UI
st.title("Talladega Testing")
st.write(label_text)

# Button click logic
if st.button(button_text):
    st.session_state.click_count += 1
    st.rerun()

