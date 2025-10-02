"""In document Loader we see two thing's page_content and meta_data."""



# from langchain_community.document_loaders import TextLoader

# loader = TextLoader('D:\LangChain\Doc_Loader\chat_history.txt')

# docs = loader.load()


# print(docs)


# print(type(docs))

# print(len(docs))

# print(docs[0])

# print(type(docs[0]))

# print(docs.page_content)

# print(docs.meta_data)






"""Now you can use any type

examples - in the above code we extract the text from 
           a text file and send that text into the llm."""
           
           


from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate



load_dotenv()


model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")


prompt = PromptTemplate(
    template = "write a summary about \n {poem}",
    input_variables = ['poem']
)


parser = StrOutputParser()


loader = TextLoader('D:\LangChain\Doc_Loader\chat_history.txt')


docs = loader.load()


chain = prompt | model | parser

result = chain.invoke({'poem': docs[0].page_content})


print(result)