from openai import OpenAI
import streamlit as st

# Load the API key
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

def analyze_compatibility(user1_data, user2_data):
    prompt = (
        """Evaluate the compatibility between two individuals by analyzing their responses to the following questions. 
        Focus on aspects such as shared values, communication styles, alignment of life goals, and any potential areas of conflict. 
        Offer a comprehensive analysis that identifies compatibility strengths, areas where they complement each other, and possible challenges they may face. 
        Conclude with insights on how these dynamics may shape their relationship."""
    )

    for q1, q2 in zip(user1_data['answers'], user2_data['answers']):
        prompt += f"Question: {q1['question']}\n"
        prompt += f"Person 1 ({user1_data['name']}): {q1['answer']}\n"
        prompt += f"Person 2 ({user2_data['name']}): {q2['answer']}\n\n"
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a relationship expert."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        n=1,
        temperature=0.7
    )
    
    output_text = response.choices[0].message.content
    return output_text

def summarize_individual_results(user_name, user_answers):
    """Summarize individual results using OpenAI GPT."""
    prompt = (
        f"Analyze the relationship preferences and values of {user_name} based on their answers to the following questions. "
        "Provide a summary of their ideal relationship dynamics, key values, and potential areas of focus or growth in relationships.\n\n"
    )

    for qa in user_answers:
        prompt += f"Question: {qa['question']}\n"
        prompt += f"Answer: {qa['answer']}\n\n"
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o",  # Use "gpt-3.5-turbo" as needed
        messages=[
            {"role": "system", "content": "You are a relationship expert."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        n=1,
        temperature=0.7
    )

    output_text = response.choices[0].message.content
    return output_text
