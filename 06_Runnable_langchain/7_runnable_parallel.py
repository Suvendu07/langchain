""" To uderstand this let take a example
topic: AI
1. send the  query to llm1 to generate a twit on the topic
2. send the querry to llm2 to generate a linkdin post on the topic
"""

""" In runnableparrllel producing a dict of output"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel, RunnableSequence

load_dotenv()


prompt1 = PromptTemplate(
    template = "Generate a tweet about {topic}",
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = "Generate a linkedin post about {topic}",
    input_variables = ['topic']
)

parser = StrOutputParser()


model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")


parallel_chain = RunnableParallel({
    
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser)
})


result = parallel_chain.invoke({'topic':'AI'})


print(result)