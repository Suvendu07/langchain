from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

st.header("Research Tool")


model = ChatOpenAI(model = 'gpt-4')

user_inputs = st.text_input("Enter your input: ")

if st.button('summarize'):
    result = model.invoke(user_inputs)
    st.write(result.content)
    

  
# it's not for run due to not provide the openai API  



# from langchain_openai import ChatOpenAI
# from langchain.prompts import PromptTemplate

# # 1. Load LLM (OpenAI here)
# llm = ChatOpenAI(model="gpt-3.5-turbo")

# # 2. Define a STATIC prompt (instruction fixed)
# prompt = PromptTemplate(
#     input_variables=["text"],
#     template="Summarize the text in 3 lines:\n{text}"
# )

# # 3. Format the prompt with user text
# user_text = "Artificial Intelligence is transforming industries. It helps automate tasks, improve decision making, and create new opportunities for businesses worldwide."
# final_prompt = prompt.format(text=user_text)

# # 4. Pass to LLM
# response = llm.predict(final_prompt)

# print("🔹 Final Prompt Sent:", final_prompt)
# print("🔹 Model Response:", response)


"""In static prompts:

The template/instruction is always the same.

Even if the user gives input in 5 lines, 10 lines, or 100 lines → the model will still summarize in 3 lines (because the instruction is fixed).

👉 That’s why it’s called static — the job description doesn’t change, only the data changes."""





# Dynamic Promt:

# import streamlit as st
# from langchain_openai import ChatOpenAI
# from langchain.prompts import PromptTemplate

# # OpenAI LLM (replace with your API key in .env or directly)
# llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# st.title("Dynamic Prompt Demo 🚀")

# # User input for instruction
# task = st.text_input("Enter your task (e.g., Summarize in 2 lines, Translate to French, Explain like a teacher):")

# # User input for text
# user_text = st.text_area("Enter your text:")

# if st.button("Generate Response"):
#     if task and user_text:
#         # Dynamic Prompt
#         prompt_template = PromptTemplate(
#             input_variables=["task", "text"],
#             template="Perform the following task: {task}\n\nHere is the text:\n{text}"
#         )
        
#         final_prompt = prompt_template.format(task=task, text=user_text)
        
#         # LLM call
#         response = llm.invoke(final_prompt)
        
#         st.subheader("Response:")
#         st.write(response.content)
#     else:
#         st.warning("Please enter both a task and some text!")
