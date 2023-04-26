import openai
from dotenv import load_dotenv
import os
from flask import Flask, Response, request, jsonify, render_template
from flask_cors import CORS
import time

load_dotenv()
OPEN_AI_API = os.getenv("OPEN_AI_API")

openai.api_key = OPEN_AI_API


def Completion(prompt):
    global response
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        stop=".",
        temperature=0.5,
        presence_penalty=0,
        frequency_penalty=0,
        max_tokens=256,
    )

    print(response["choices"][0]["text"])


app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat")
def chat():
    return render_template("chat.html")


@app.route("/resp", methods=["POST"])
def resp():
    data = request.get_json()
    prompt = data["prompt"]
    Completion(prompt)

    time.sleep(5)
    return jsonify({"response": response["choices"][0]["text"] + "."})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
