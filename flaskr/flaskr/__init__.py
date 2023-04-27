import sys
# caution: path[0] is reserved for script path (or '' in REPL)
from encryption_algorithm import ecsda
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/encrypt', methods=['POST'])
def encrypt_document():
    # Get the uploaded document from the request
    file = request.files['file']

    # Call the encryption algorithm
    encrypted_document = encryption_algorithm.encrypt(file.read())

    # Return the encrypted document as a response
    return jsonify({'encrypted_document': encrypted_document})

if __name__ == '__main__':
    app.run(debug=True)