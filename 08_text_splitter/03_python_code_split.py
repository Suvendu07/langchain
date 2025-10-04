from langchain.text_splitter import RecursiveCharacterTextSplitter, Language


text = """
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("D:\LangChain\Pdf of langchain\LangChain_Prompts_Explanation.pdf")


docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator = ''
)

result = splitter.split_documents(docs)



print(result[0].page_content)"""


splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON, # you can use any language.
    chunk_size = 300,
    chunk_overlap = 0
)



chunk = splitter.split_text(text)


print(chunk[0])