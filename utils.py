import json
import os
import random
import string
from constants import questions,options

def generate_unique_key():
    """Generate a 5-digit unique key."""
    while True:
        key = ''.join(random.choices(string.digits, k=5))
        if key not in load_user_data():
            return key

def load_user_data():
    """Load user data from JSON file."""
    if os.path.exists('user_data.json'):
        with open('user_data.json', 'r') as f:
            return json.load(f)
    return {}

def save_user_data(user_name,user_email, user_answers):
    """Save user data to JSON file and generate a unique key."""
    user_data = load_user_data()
    unique_key = generate_unique_key()
    user_data[unique_key] = {
        'name': user_name,
        "mail": user_email,
        'answers': [
            {
                'question': questions[q_id],
                'answer': answer
            } for q_id, answer in user_answers.items()
        ]
    }
    with open('user_data.json', 'w') as f:
        json.dump(user_data, f, indent=4)
    return unique_key