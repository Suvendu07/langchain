# this code is just for my pratice(demo) bcz of i can;t access the api key due to paid of cost.
# the api is key is in D:\LangHhain\venvlangchain\.env this path. we store the api key in this file bcz of seafty. bcz no can acces this.


# this is the lin where langchain know that how to talk with the openai(langchain_openai)
from langchain_openai import OpenAI
from dotenv import load_dotenv  # it is used for dw the api key from secreat .env file

load_dotenv()

llm = OpenAI(model = 'gpt-3.5-turbo-instruct') # here we provide to which model of openai we inteact

result = llm.invoke("what is the capital of india") # for use of this method we communicate with gpt model
# the invoke method hot the model and send the promt to the gpt model and give the response



print(result)

# in LLMS take a string (or plain text) as i/p and returns a string a sting(plain text)



# but in today we don't use llm so that insted of use this we use a new model called chatmodel