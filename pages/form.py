import streamlit as st
import re

st.set_page_config(
    page_title="Simple Form",
    page_icon=":smiley:",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "Simple Streamlit demo app"
    }
)

st.title("User Registration Form")

def is_valid_mail(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

with st.form("registration_form"):
    st.subheader("Please fill in the details below:")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    is_student = st.checkbox("Are you a student?")
    submit_button = st.form_submit_button("Register")

    if submit_button:
        errors = []
        if not name.strip():
            errors.append("Name is required.")
        if not email.strip():
            errors.append("Email is required.")
        elif not is_valid_mail(email):
            errors.append("Invalid email format.")
        if not password:
            errors.append("Password is required.")
        elif password != confirm_password:
            errors.append("Passwords do not match.")
        if errors:
            for error in errors:
                st.error(error)
        else:
            # Simulate saving data
            user_data = {
                "name": name,
                "email": email,
                "age": age,
            }

            st.success("✅ Registration successful!")

            st.dataframe(user_data)














