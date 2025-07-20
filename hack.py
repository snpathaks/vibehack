# app.py
# Import necessary components from Flask and Flask-SocketIO
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import os
import requests  # Use requests library to call Gemini API
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# --- Configuration ---
# This API key will now be used for the Gemini API
API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

# Create an instance of the Flask class and configure SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_very_secret_key!'
socketio = SocketIO(app)

# In-memory "database" for user profiles
profiles = {}

# --- Standard HTTP Routes ---
@app.route('/')
def home():
    """Renders the main landing page."""
    return render_template('index.html')

@app.route('/study-groups')
def study_groups():
    """Renders the study group platform page."""
    return render_template('study_group_platform.html')

@app.route('/api/profile', methods=['POST'])
def save_profile():
    """API endpoint to save a user's profile."""
    data = request.get_json()
    if not data or 'studentName' not in data:
        return jsonify({'status': 'error', 'message': 'No data provided!'}), 400
    student_name = data['studentName']
    profiles[student_name] = data
    print("Profile received and saved:", profiles[student_name])
    return jsonify({'status': 'success', 'message': f'Profile for {student_name} saved successfully!'})


# --- WebSocket Event Handler for the AI Chatbot (Now with Gemini) ---
@socketio.on('chatbot_message')
def handle_chatbot_message(json_data):
    """
    Handles messages sent to the chatbot.
    It constructs a prompt, calls the Gemini API, and emits the response.
    """
    user_message = json_data['message']
    print(f"Received message for Gemini: {user_message}")

    emit('bot_response', {'message': "🧠 Thinking..."})

    # Construct a detailed prompt for the Gemini API
    prompt = (f"As an expert academic advisor, please suggest 3 popular books and 3 recent, relevant research papers "
              f"for a university student studying the topic: '{user_message}'. "
              f"Please format the response in simple HTML with headings (e.g., <h3>) and unordered lists (<ul>, <li>). "
              f"Do not include markdown like ```html.")

    # Prepare the payload for the Gemini API
    payload = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }]
    }
    headers = {'Content-Type': 'application/json'}

    try:
        # Call the Gemini API
        response = requests.post(GEMINI_API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        result = response.json()
        
        # Extract the text from the Gemini response
        if (result.get('candidates') and result['candidates'][0].get('content') and
                result['candidates'][0]['content'].get('parts')):
            bot_reply = result['candidates'][0]['content']['parts'][0]['text']
        else:
            bot_reply = "Sorry, I couldn't process that request. The response from the AI was empty."

    except requests.exceptions.RequestException as e:
        print(f"Error calling Gemini API: {e}")
        bot_reply = "Sorry, I'm having trouble connecting to the AI service right now. Please try again later."
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        bot_reply = "An unexpected error occurred. Please check the server logs."

    # Send the formatted response back to the client
    emit('bot_response', {'message': bot_reply})


# This block runs the app with SocketIO support
if __name__ == '__main__':
    socketio.run(app, debug=True)
