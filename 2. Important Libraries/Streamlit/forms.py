import streamlit as st

with st.form("form_key"):

    st.write("What would you like to order")

    appetizer = st.selectbox(
        "Appetizers",
        options=["choice1", "choice2", "choice3"]
    )

    main_course = st.selectbox(
        "Main Course",
        options=["choice1", "choice2", "choice3"]
    )

    dessert = st.selectbox(
        "Dessert",
        options=["choice1", "choice2", "choice3"]
    )

    ice_cream = st.checkbox("Are you bringing Ice Cream")

    visit_date = st.date_input("When are you coming?")

    visit_time = st.time_input("At what time are you coming")
    
    allergies = st.text_area("Any allergies?", placeholder="Leave us a note for allergies")

    submit = st.form_submit_button("Submit")

st.write(
    f"""
    Your Order Summary:

    Appetizer: {appetizer}
    Main Course: {main_course}
    Dessert: {dessert}

    Are your bringing your own icecream: {"yes" if ice_cream else "no"}
    Date of Visit: {visit_date}
    Time of Visit: {visit_time}

    Allergies: {allergies}
    """
)