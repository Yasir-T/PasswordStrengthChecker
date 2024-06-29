from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)

def password_strength(password):
    strength = 0
    conditions = [
        r".{8,}",             # At least 8 characters
        r"[a-z]",             # At least one lowercase letter
        r"[A-Z]",             # At least one uppercase letter
        r"[0-9]",             # At least one digit
        r"[\W_]",             # At least one special character
    ]

    # Check each condition and update the strength score
    for condition in conditions:
        if re.search(condition, password):
            strength += 1

    return strength

def get_strength_level(strength):
    levels = {
        0: "Very Weak",
        1: "Weak",
        2: "Moderate",
        3: "Strong",
        4: "Very Strong",
        5: "Excellent"
    }
    return levels.get(strength, "Unknown")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_password():
    data = request.get_json()
    password = data.get('password', '')
    strength = password_strength(password)
    strength_level = get_strength_level(strength)
    return jsonify({'strength': strength_level})

if __name__ == "__main__":
    app.run(debug=True)
