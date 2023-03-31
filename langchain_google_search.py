import os
import config
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

# Put your OpenAI API key in the environment variable OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = config.openaikey

#Put your Serp API key in the environment variable SERPAPI_API_KEY
os.environ["SERPAPI_API_KEY"] = config.serpapikey

llm = OpenAI(temperature=0) # type: ignore

tools = load_tools(["serpapi","llm-math"], llm=llm)
agent = initialize_agent(tools,llm,agent="zero-shot-react-description",verbose=True)

# Get response form input then agent.run(input)
while True:
    user_input = input("What is your question? (type \"exit\" to quit): ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break 
    else:
        agent.run(user_input)