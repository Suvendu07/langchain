from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")


while True:
    user_input = input('you:')
    if user_input == 'exit':
        break
    
    result = model.invoke(user_input)
    
    print("AI: ",result.content)
    
    
"""in this code having one probelm
you: which one is grater number 2 or 0
AI: 2

you: now multiply the bigger number by 10
AI: Let's say the bigger number is x.

Multiply the x by 10, we get 

10x


problem is that when we say that which one is bigger 
it say that 2 and when we say multiply with the bigger number
it take the bigger number is x.


problem is happen due to in our code having no context means no memory

to solve this change the code in below: """



from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")

chat_history = []

while True:
    user_input = input('you:')
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    
    print("AI: ",result.content)
    
    
print(chat_history)



"""but we have a problem when we see the chat_history o/p we know that 
who give which message

to solve this langchain have a built-in method."""



from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")

chat_history = [
    SystemMessage(content = "you are a helpful Ai assistant")
]

while True:
    user_input = input('you:')
    chat_history.append(HumanMessage(content = user_input))
    if user_input == 'exit':
        break
    
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content = result.content))
    
    print("AI: ",result.content)
    
    
print(chat_history)