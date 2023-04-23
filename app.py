import openai
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
OPEN_AI_API = os.getenv("OPEN_AI_API")

prompt = "What is Kulthe Media?"
print(prompt)
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
