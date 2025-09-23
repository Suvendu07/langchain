from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


load_dotenv()


# the dimension represented that how much dimension o/p do you want 
embedding = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions = 32)


documents = [
    "Delhi is the capital of india",
    "bbsr is capital of odisha",
    "Kolkata is capital of WB"
]


result = embedding.embed_documents(documents)

print(str(result))


# it's not for run due to paid API key