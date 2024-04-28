from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a dictionary to store valid authentication tokens
valid_tokens = {
    "123456": "user_id_123456"
}

# Route to handle authentication requests
@app.route('/authenticate', methods=['POST'])
def authenticate():
    token = request.headers.get('Authorization')

    # Check if the token is valid
    if token in valid_tokens:
        user_id = valid_tokens[token]
        return jsonify({'success': True, 'user_id': user_id})
    else:
        return jsonify({'success': False, 'message': 'Invalid token'}), 401

if __name__ == '__main__':
    # Run Flask app with SSL enabled
    app.run(ssl_context='adhoc', debug=True)
