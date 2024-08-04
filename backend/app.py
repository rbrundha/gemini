from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def generate_text(prompt):
    # Set the API key
    api_key = "AIzaSyAdFVWxjjIpKBe1SugTIt6XmomWtv6CWLI"
    
    # URL for the Gemini model endpoint
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"

    # Prepare the payload
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    # Set headers
    headers = {
        "Content-Type": "application/json"
    }

    # Make the POST request
    response = requests.post(url, headers=headers, json=payload)
    
    # Log the response for debugging
    print(f"Response status code: {response.status_code}")
    print(f"Response content: {response.content.decode('utf-8')}")
    
    # Check if the request was successful
    if response.status_code == 200:
        response_json = response.json()
        # Log the actual response JSON
        print(f"Response JSON: {response_json}")
        # Return the response JSON directly
        return response_json
    else:
        return {
            "error": f"Error: {response.status_code} - {response.text}"
        }

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt')
    generated_text = generate_text(prompt)
    return jsonify(generated_text)

# Add a root endpoint for GET requests
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Gemini Text Generation API!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')