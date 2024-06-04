from flask import Flask, request, jsonify, send_file
import requests
import os

app = Flask(__name__)

REMOVE_BG_API_KEY = "4pRdM8TsUoiL5vDfatLgMRcy"
REMOVE_BG_URL = 'https://api.remove.bg/v1.0/removebg'

@app.route('/remove', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        response = requests.post(
            REMOVE_BG_URL,
            headers={'X-Api-Key': REMOVE_BG_API_KEY},
            files={'image_file': file},
            data={'size': 'auto'}
        )

        if response.status_code == requests.codes.ok:
            output_path = 'output.png'
            with open(output_path, 'wb') as out_file:
                out_file.write(response.content)
            return send_file(output_path, mimetype='image/png')
        else:
            return jsonify({"error": response.text}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
