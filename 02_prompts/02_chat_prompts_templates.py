from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage



chat_templates = ChatPromptTemplate([
    ('system', "you are a helpful {domain} expert"),
    ('Human', "Explain in simple terms, what is {topic}"),
    # SystemMessage(content = "you are a helpful {domain} expert"),
    # HumanMessage(content = "Explain in simple terms, what is {topic}")
])


prompt = chat_templates.invoke({'domain':'cricket','topic':'Dusra'})


print(prompt)


# This is dynamic set of message for chatprompts