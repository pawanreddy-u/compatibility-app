import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests
import logging
from constants import questions, options
from utils import generate_unique_key, load_user_data, save_user_data
from main import analyze_compatibility, summarize_individual_results

# Configure root logger to only display ERROR level and above
logging.basicConfig(level=logging.ERROR, format="%(levelname)s: %(message)s")

# Create a custom logger for your app
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        logger.error("Failed to load Lottie animation")
        return None
    return r.json()

def self_assessment():
    st.header("Self Assessment")
    lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
    st_lottie(lottie_hello, height=200, key="hello")

    user_name = st.text_input("Enter your name", key="name_input")
    user_email = st.text_input("Enter your email id", key="email_input")
    user_answers = {}
    st.write("")  # Add some space

    st.markdown("### Please answer the following questions:")
    st.write("")  # Add some space

    with st.form(key='assessment_form'):
        for q_id, question in questions.items():
            st.markdown(f"**{q_id}. {question}**")
            user_answers[q_id] = st.radio("", options[q_id], key=f"q_{q_id}")
            st.write("")  # Add some space

        submit_button = st.form_submit_button(label='Save Answers')

    if submit_button:
        if user_name and all(user_answers.values()):
            logger.info(f"Saving answers for user: {user_name}")
            unique_key = save_user_data(user_name, user_email, user_answers)
            st.success(f"Answers saved for {user_name}. Your unique key is: {unique_key}")
            logger.info(f"Answers saved for {user_name} with email {user_email}. Your unique key is: {unique_key}")
            st.info("Please save this key to compare your results later.")
            
            with st.spinner("Generating your relationship profile..."):
                summary = summarize_individual_results(
                    user_name, [{'question': questions[q_id], 'answer': answer} for q_id, answer in user_answers.items()]
                )
            st.subheader("Your Relationship Profile Summary")
            logger.info(f"Your Relationship Profile Summary:{summary}")

            st.write(summary)
        else:
            st.warning("Please enter your name and answer all questions.")

def compatibility_comparison():
    st.header("Compatibility Comparison")
    lottie_compare = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_khzniaya.json")
    st_lottie(lottie_compare, height=200, key="compare")

    col1, col2 = st.columns(2)
    with col1:
        key1 = st.text_input("Enter the first person's unique key")
    with col2:
        key2 = st.text_input("Enter the second person's unique key")

    if st.button("Compare Compatibility"):
        if key1 and key2 and key1 != key2:
            logger.info(f"Comparing compatibility for keys: {key1} and {key2}")
            user_data = load_user_data()
            if key1 in user_data and key2 in user_data:
                try:
                    with st.spinner("Analyzing compatibility..."):
                        result = analyze_compatibility(user_data[key1], user_data[key2])
                    st.subheader(f"Compatibility Analysis: {user_data[key1]['name']} and {user_data[key2]['name']}")
                    logger.info(f"Compatibility analysis:{result}")
                    st.write(result)
                except Exception as e:
                    logger.error(f"Error during compatibility analysis: {e}")
                    st.error("An error occurred. Please try again.")
            else:
                st.warning("One or both keys are invalid. Please check and try again.")
        else:
            st.warning("Please enter two different valid keys for comparison.")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Relationship Compatibility App", page_icon="💑", layout="wide")
    local_css("styles/style.css")

    st.title("Relationship Compatibility App")

    selected = option_menu(
        menu_title=None,
        options=["Self Assessment", "Compatibility Comparison"],
        icons=["person-check", "people"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )

    if selected == "Self Assessment":
        self_assessment()
    elif selected == "Compatibility Comparison":
        compatibility_comparison()

if __name__ == "__main__":
    main()