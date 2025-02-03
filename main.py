from dotenv import load_dotenv
import os
# import langgraph
from langchain_openai import ChatOpenAI

# Get OpenAI API key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPEN_AI_KEY")
# print(OPENAI_API_KEY)
os.environ["OPENAI_API_KEY"]=OPENAI_API_KEY

# Initialize OpenAI Chat Model
llm = ChatOpenAI(model="gpt-4o")

while True:
    print(llm.invoke("Hey there!").content)
    prompt =input("Type Here: ")
    response = llm.invoke(prompt)
    print(response.content)