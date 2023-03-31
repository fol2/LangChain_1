import os
import config
from langchain import OpenAI, ConversationChain

# Put your OpenAI API key in the environment variable OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = config.openaikey

llm = OpenAI(temperature=0.5) # type: ignore
conversation = ConversationChain(llm=llm, verbose=False) #change verbose to True to see the output of the model

# Get response form input then agent.run(input)
user_name = input("What's your name? ")
i = 0
while True:
    user_input = input(user_name + ": ")
    if user_input.lower() == "exit":
        print("AI: Goodbye!")
        break 
    else:
        print("AI: " + conversation.predict(input = user_input))
        i += 1
        if i == 10:
            print("(Type 'exit' to quit)")
            i = 0