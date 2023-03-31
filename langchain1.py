import os
from langchain.llms import OpenAI
import config

# Put your OpenAI API key in the environment variable OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = config.openaikey


llm = OpenAI(temperature=0.9)

text = "What is the meaning of life?"
print(llm(text))