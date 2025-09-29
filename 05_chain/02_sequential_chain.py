""" let take a example's to understand it 

1. take the user's input.
2. send to the llm.
3. get the ans from llm.
4. again send the ans to the llm.
5. say that summarize this ans.
6. get your ans."""


from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


prompt1 = PromptTemplate(
    template = "Generate a detailed report on {topic}",
    input_variables = ['topic']
)


prompt2 = PromptTemplate(
    template = "Generate a 5 pointer summary from the folling text \n {text}",
    input_variables = ['text']
)

model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")


parser = StrOutputParser()


chain = prompt1 | model | parser | prompt2 | model | parser


result = chain.invoke({'topic':'Unemployement in India'})


print(result)

# chain.get_graph().print_ascii()