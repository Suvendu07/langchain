from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field



load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-2-2b-it",
    task = "text-generation"
)


model = ChatHuggingFace(llm - llm)



class Person(BaseModel):
    
    name: str = Field(description = "name of the person")
    age: int = Field(description = "age of the person")
    city: str = Field(description = "name of the city the person belong's to")
    
    
parser = PydanticOutputParser(pydantic_object = Person)

template = PromptTemplate(
    template = "Generate the namem age and city of a frictional {place} person \n {format_instruction}",
    input_variables = ['place'],
    partial_variables = {'format_instruction': parser.get_format_instruction()}
)


# prompt = template.invoke({'place':'indian'})

# result = model.invoke(prompt)

# result = parser.parse(result.content)


chain = template | model | parser

result = chain.invoke({'place':'indian'})

print(result)