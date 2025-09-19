from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = 'gpt-4')

# model = ChatOpenAI(model = 'gpt-4', temperature = 0, max_completion_tokens = 10)

result = model.invoke("what is the capital of india")

print(result)

# print(result.content)

# this code is not for run bcz of i did't provided the API.