import streamlit as st
from streamlit_option_menu import option_menu
import login
import recommend  # Import the recommendation module

st.set_page_config(
    page_title="PawSome-AI",
    page_icon="🐾",
    layout="centered",
    initial_sidebar_state="auto"
)

# Initialize session state for login
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Display login form or main interface based on login status
if not st.session_state['logged_in']:
    login.login()
else:
    # Display sidebar with options
    with st.sidebar:
        selected = option_menu(
            'PawSome AI',
            ['Welcome', 'Disease & Breed Detection', 'Petcare ChatBot', 'Prescription-Analyzer', 'Health Recommendation', 'Team Details', 'Feedback', 'Logout'],
            icons=['house-door-fill', 'search', 'chat-right-fill', 'file-earmark-break-fill', 'info', 'star', 'box-arrow-right'],
            menu_icon="🐶",
            default_index=0
        )

    # Render the appropriate page based on selection
    if selected == 'Welcome':
        import welcome
        welcome.welcome()

    elif selected == 'Disease & Breed Detection':
        import model
        model.model()

    elif selected == 'Petcare ChatBot':
        import chatbot
        chatbot.chatbot()

    elif selected == 'Prescription-Analyzer':
        import prescription
        prescription.presc_analyze()

    elif selected == 'Health Recommendation':
        st.subheader("Health Recommendation")

        # Text input fields for symptoms
        symptoms = {
            'symptoms1': st.text_input('Symptom 1'),
            'symptoms2': st.text_input('Symptom 2'),
            'symptoms3': st.text_input('Symptom 3'),
            'symptoms4': st.text_input('Symptom 4'),
            'symptoms5': st.text_input('Symptom 5')
        }

        # Button to get the recommendation
        if st.button("Get Recommendation"):
            # Call the recommendation function from recommend.py
            result = recommend.get_recommendation(symptoms)
            st.write("Health Status:", result)

    elif selected == 'Feedback':
        import feedback
        feedback.feedback()

    elif selected == 'Team Details':
        import team
        team.team_details()

    elif selected == 'Logout':
        login.logout()
        login.login()
