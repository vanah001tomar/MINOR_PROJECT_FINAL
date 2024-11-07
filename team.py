import streamlit as st
import webbrowser

def team_details():
    st.title("Our Team")

    team_members = [
        {
            "name": "Harsh Vardhan",
            "gmail": "vardhanharsh7906@gmail.com",
        },
        {
            "name": "Swapnil",
            "gmail": "vashutyagi20@gmail.com",
        },
        {
            "name": "Vansh Tomar",
            "gmail": "vanshikatmar@gmail.com",
        },


    ]

    for member in team_members:
        st.header(member["name"])
        if st.button(f"Contact {member['name']} via Gmail"):
            webbrowser.open_new_tab(f"mailto:{member['gmail']}?subject=Regarding%20PawSome-AI%20App")

if __name__ == "__main__":
    team_details()
