from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-2-2b-it",
    task = "text-generation"
)


model = ChatHuggingFace(llm = llm)

parser = JsonOutputParser()


template1 = PromptTemplate(
    template = "give me the name, age, and city of a fictional person \n {format_instruction}",
    input_variables = [],
    partial_variables = {'format_instruction': parser.get_format_instructions()}
)


# prompt = template1.format()
# print(prompt)

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

""" Insted of write these above three lines, we use chain rule"""

chain = template1 | model | parser

result = chain.invoke({})

print(result)

print(type(result))




""" In this jsonparser happen one problem that it not provide the schema enforce,
means you can't decide the structure of json file. it decide the llm.



To solve this use structured_output_parsers."""