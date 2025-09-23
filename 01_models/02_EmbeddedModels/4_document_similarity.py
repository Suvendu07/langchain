from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


load_dotenv()

embedding = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions = 300)


documents = ['i am suvendu khuntia',
             'i am from jajpur',
             'i know ML, DL, Langchain, python',
             'i am belonging a agricultural family',
             ]


querry = "tell me about suvendu"

doc_embedding = embedding.embed_documents(documents)
querry_embedding = embedding.embed_query(querry)


scores = cosine_similarity([querry_embedding], doc_embedding)[0]

index, score = sorted(list(enumerate(scores)), key = lambda x:x[1])[-1]


print(querry)
print(documents[index])
print("similarity score is: ", score)