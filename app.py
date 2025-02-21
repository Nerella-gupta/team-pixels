import requests


def send_message_flask(user_text, treatment):
    API_URL = "http://localhost:5000/api/chat"
    try:
        response = requests.post(API_URL, json={"userInput": user_text, "treatmentType": treatment})
        if response.status_code == 200:
            print(response.json())  # Debugging line
            return response.json()["response"]
        else:
            return "Error: Unable to connect to AI Chatbot."
    except requests.exceptions.RequestException:
        return "Error: AI server is down or unreachable."

def send_message_gemini(user_text):
    try:
        genai.configure(api_key=st.secrets["AIzaSyBCHKrdkObNnd9nxY6go28U7DkVuICDRrc"])  # type: ignore # Use Streamlit secrets for security
        model = genai.GenerativeModel('gemini-1.5-flash') # type: ignore
        response = model.generate_content(user_text)
        print(response.text)  # Debugging line
        return response.text
    except Exception as e:
        return f"Error: {e}"