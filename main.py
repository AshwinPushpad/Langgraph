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

# Only using OpenAI
# from openai import OpenAI
# client = OpenAI()
#
# completion = client.chat.completions.create(
#   model="gpt-4o",
#   messages=[
#     {"role": "developer", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Hello!"}
#   ]
# )
#
# print(completion.choices[0].message.content)

while True:
    print(llm.invoke("Hey there!").content)
    prompt =input("Type Here: ")
    response = llm.invoke(prompt)
    print(response.content)