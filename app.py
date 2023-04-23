import openai
from dotenv import load_dotenv
import os
from flask import Flask, Response, request, jsonify, render_template
from flask_cors import CORS

load_dotenv()
OPEN_AI_API = os.getenv("OPEN_AI_API")


def Completion(prompt):
    global response
    response = openai.Completion.create(
        model="davinci:ft-kulthe-media-2023-04-08-19-23-11",
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


@app.route("/resp", methods=["POST"])
def resp():
    data = request.get_json()
    prompt = data["prompt"]
    Completion(prompt)

    return jsonify({"response": response["choices"][0]["text"] + "."})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
