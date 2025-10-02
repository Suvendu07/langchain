"""It is use in case of folder.

like when you have a folder and inside that folder having many pdf, and
you want to load all pdf at the same time. in that time we use this directory_loader."""


# from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader


# loader = DirectoryLoader(
#     path = "D:\Learning schedule",
#     glob = '*.pdf',
#     loader_cls = PyPDFLoader
# )

# docs = loader.load()

# print(docs)

# print(len(docs))

# print(docs[0].page_content)

# print(docs[0].metadata)




"""In this doc_loader there having are some problem:
1. it take time to load the pdf bcz to load a folder and inside that having many pdf.

2. at the same time all are store in memory.


To solve this prob. there is a solution in langchain called lazy_load"""


from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader


loader = DirectoryLoader(
    path = "D:\Learning schedule",
    glob = '*.pdf',
    loader_cls = PyPDFLoader
)

docs = loader.lazy_load()

# print(docs)

# print(len(docs))

# print(docs[0].page_content)

# print(docs[0].metadata)

for doc in docs:
    print(doc.metadata)