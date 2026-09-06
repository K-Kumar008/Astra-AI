from flask import Flask, request, jsonify, send_from_directory
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(
    api_key=os.environ.get("EXPLABS_API_KEY"),
    base_url="https://api.experientiallabs.ai/v1"
)

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")

    if not message:
        return jsonify({"error": "Please enter a message"}), 400

    response = client.responses.create(
        model="gpt-6-astra",
        input=message
    )

    return jsonify({"reply": response.output_text})

if __name__ == "__main__":
    app.run(debug=True)


                                                                                     [ Read 32 lines ]
^G Help          ^O Writ
