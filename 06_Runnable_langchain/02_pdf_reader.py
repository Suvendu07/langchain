from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import openai



loader = TextLoader("doc.txt") # ensure docs.txt exists
document = loader.load()


# split the text into smaller chunks
texts_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)
docs = texts_splitter.split_documents(document)


# convert text into embedding & store in FAISS
vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())


# create a retriver (fetches relevent documents)
retriver = vectorstore.as_retriver()


# mannualy retrivers relevent documents
query = "What are the key takeways from the documents?"
retrived_docs = retriver.get_relevent_documents(query)


# combine retrived text into a single prompt
retrived_text = "\n".join([docs.page_content for doc in retrived_docs])


# initialize the llm
llm = openai(model_name = "gpt-3.5-turbo", temperature = 0.7)

# Manually pass retrived text to LLM
prompt = f"Based on the following text, answer the question: {query}\n\n{retrived_text}"
answer = llm.predict(prompt)


# print the answer
print("Answer: ", answer)



""" This code is not for run."""