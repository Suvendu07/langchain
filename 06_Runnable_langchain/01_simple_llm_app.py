from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()


llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")


prompt = PromptTemplate(
    template = "Suggest a catchy blog title about {topic}",
    input_variables = ['topic']
)


topic = input("enter a topic: ")


# Format the prompt manually using prompttemplate
fomatted_prompt = prompt.format(topic = topic)


# call the llm directly
blog_title = llm.predict(fomatted_prompt)


# print the output
print("Generate Blog Title: ", blog_title)