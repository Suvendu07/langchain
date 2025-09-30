from langchain.llms import openai
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


llm = openai(model = "gpt-3.5-turbo", temperature = 0.7)


prompt = PromptTemplate(
    input_variables = ['topic'],
    template = "Suggest a catchy blog title about {topic}"
)



chain = LLMChain(llm = llm, prompt = prompt)


topic = input("enter a topic: ")
output = chain.run(topic)


print("Generate Blog title: ", output)


# This code id not for run