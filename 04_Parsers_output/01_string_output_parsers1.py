from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


model = ChatOpenAI()


# 1st prompt
template1 = PromptTemplate(
    template = 'write  detailed report on {topic}',
    input_variables = ['topic']
)

template2 = PromptTemplate(
    template = 'write a 5 line summary on the following text /n {text}',
    input_variables = ['text']
)


parsers = StrOutputParser()


""" This line means 1st take the question and send to the model generate only the 
respone no meta data with the help of parsers. This is chain format."""
chain = template1 | model | parsers | template2 | model | parsers

result = chain.invoke({'topic':'black hole'})

print(result)