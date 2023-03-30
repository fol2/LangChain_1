pip install langchain

pip install openai

import os
from langchain.llms import OpenAI

# Put your OpenAI API key in the environment variable OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


llm = OpenAI(temperature=0.9)

text = "The quick brown fox jumps over the lazy dog."
print(llm(text))