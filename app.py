import openai
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
OPEN_AI_API = os.getenv("OPEN_AI_API")

df = pd.read_csv("booth.ai.csv")
print(f"Sample Heading => \n{df.head()}")
