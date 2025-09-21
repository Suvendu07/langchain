# the model is dw in locally
from langchain_huggingface import HuggingFaceEmbeddings


embedding = HuggingFaceEmbeddings(model_name = 'sentance-transformers/all-MiniLM-L6-v2')


text = "Delhi is the capital of india"

result = embedding.embed_query(text)

print(str(result))


# you can do in multiple docments