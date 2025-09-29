from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel,Field
from typing import Literal




load_dotenv()



model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")



parser = StrOutputParser()



class Feedback(BaseModel):
    
    sentiment: Literal['positive','negetive'] = Field(description = "Give the sentiment of the feedback")




parser_2 = PydanticOutputParser(pydantic_object=Feedback)



prompt_1 = PromptTemplate(
    template = "Classify the sentiment of the following feedback into positive or negative \n {feedback} \n {format_instruction}",
    input_variables = ['feedback'],
    partial_variables = {'format_instruction':parser_2.get_format_instructions()}
)





classifier_chain = prompt_1 | model | parser_2




prompt_2 = PromptTemplate(
    template = "Write an appropiate response to this positive feedback \n {feedback}",
    input_variables = ['feedback']
)





prompt_3 = PromptTemplate(
    template = "Write an appropiate response to this negative feedback \n {feedback}",
    input_variables = ['feedback']
)




branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt_2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt_3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment" ) 
)


chain = classifier_chain | branch_chain

result = chain.invoke({'feedback': "this is a wonderfull phone"})

print(result)