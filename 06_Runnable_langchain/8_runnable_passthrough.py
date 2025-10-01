""" It is special type of runnable primitive that simply returns the input as output without modifying it"""

"""
Prompt-llm-parser
1. runnablepassthrough
2. prompt2-llm-parser"""


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.schema.runnable import RunnablePassthrough, RunnableParallel, RunnableSequence


load_dotenv()

"""
# passthough = RunnablePassthrough()

# print(passthough.invoke(2))

"""


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



joke_gen_chain = RunnableSequence(prompt1, model, parser)



parallen_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})



final_chain = RunnableSequence(joke_gen_chain, parallen_chain)

result = final_chain.invoke({'topic':'cricket'})

print(result)