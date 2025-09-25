from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
"""We use SystemMessage, HumanMessage, AIMessage in LangChain because:

They tell the LLM who is speaking and what their role is.

If we don’t give roles, the LLM might get confused — it may not know whether a line 
is a rule, a user question, or the assistant’s past response.

With roles, the LLM can clearly separate:

SystemMessage → permanent instruction (like “You are a polite teacher”).

HumanMessage → user input (the actual question).

AIMessage → model’s own reply (so it remembers what it said before)."""
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv


model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")


message = [
    SystemMessage(content = "you are a helpful assistant"),
    HumanMessage(content = "tell me about langchain")
]


result = model.invoke(message)


message.append(AIMessage(content = result.content))

print(message)


# we integrete this technic in our chatbot