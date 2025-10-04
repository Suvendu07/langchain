# from langchain.text_splitter import CharacterTextSplitter


# text = """you can pass text ksdakjd kahsdias askjdkas dkashiahk
# siuashdkj ashdga dashgdhuas gduya duasgteqwe gedyt gsahjdg asdjasg
# dh ash jdgauys djhasdg uasdhjkas uyasdkja uasd qiuyjj ruwye amnsdgguag
# d akjatsdua daksgdhasdlwd7iydefuy qmnwegySA ,MSADSA ASWAJEYF JHASDG """

# splitter = CharacterTextSplitter(
#     chunk_size = 10,
#     chunk_overlap = 0,
#     separator = ''
# )


# result = splitter.split_text(text)

# print(result)




""" apply text sliptting using doc_loader."""

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



print(result[0].page_content)