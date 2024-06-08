from dotenv import load_dotenv, dotenv_values 
from flask import Flask, request, jsonify
from logging.config import dictConfig
import hashlib
import os
import ssl
import time

load_dotenv() 

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": "logs/flask.log",
                "formatter": "default",
            },
        },
        "root": {"level": "DEBUG", "handlers": ["console", "file"]},
    }
)

app = Flask(__name__)

def generate_hash(salt, timestamp):
    return hashlib.sha3_256((salt + str(timestamp)).encode()).hexdigest()

# Your custom action
def perform_action(data):
    return "Action performed successfully!"

def round_to_nearest_30s(ts):
    return ts - (ts % 30)

@app.route('/api/endpoint', methods=['POST'])
def api_endpoint():
    auth_header = request.headers.get('Authorization')
    data = request.get_json()
    
    if auth_header and data:
        # Extract the token from the request
        token = auth_header.split()[-1]
        timestamp = round_to_nearest_30s(int(time.time()))

        expected_token = generate_hash(SALT, timestamp)
        
        if token == expected_token:
            # Token is valid, perform the action
            result = perform_action(data)
            return jsonify({"message": result}), 200
        else:
            # Invalid token or timestamp
            return jsonify({"error": "Unauthorized"}), 401
    else:
        # No token provided
        return jsonify({"error": "Unauthorized"}), 401

if __name__ == '__main__':
    SALT = os.getenv('SALT')
    PORT = os.getenv('PORT')
    cert_file = os.getenv('CERT_FILE')
    key_file = os.getenv('KEY_FILE')

    if os.path.exists(cert_file) and os.path.exists(key_file):
        # Run with HTTPS
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        context.load_cert_chain(cert_file, key_file)
        
        app.logger.debug('Running with SSL...')
        app.run(debug=True, host='0.0.0.0', port=PORT, ssl_context=context)
    else:
        # Run with HTTP
        app.logger.debug('Running without SSL...')
        app.run(debug=True, host='0.0.0.0', port=PORT)
