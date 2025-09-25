"""In LangChain, a MessagePlaceholder is used to create a 
flexible spot in your prompt where past conversation history
or dynamic messages can be inserted. Instead of keeping the 
prompt fixed, the placeholder acts like an empty box that will
later be filled with HumanMessage, AIMessage, or other message 
types during the conversation. This is especially useful when 
you want the model to remember previous interactions and continue
the chat naturally. For example, if you add a MessagePlaceholder 
called chat_history, LangChain will automatically insert past user
and AI messages into that space whenever the prompt runs. In simple 
words, a MessagePlaceholder works like a memory slot inside the prompt 
that helps the LLM stay aware of the conversation flow."""


# Load the chat_history.txt file to remeber the past conversation.
# But generally we store in our database


from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


# chat template

chat_templates = ChatPromptTemplate([
    ('system', 'you are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'), # use to load the previous chat in placeholder
    ('human', '{querry}')
])


chat_history = []

# load chat history
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())
    

# if u want to see the message placeholder 
# print(chat_history)  # run this
    
# create prompt
promt = chat_templates.invoke({'chat_history':chat_history, 'query':'where is my refund'})

print(promt)


# message placeholder is generally used for retrive and store the chat