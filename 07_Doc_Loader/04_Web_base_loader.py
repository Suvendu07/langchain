"""It is help to load the any webpage content"""


from langchain_community.document_loaders import WebBaseLoader


"""You can pass a list of url"""


url = 'https://www.youtube.com/watch?v=bL92ALSZ2Cg&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0&index=13'

loader = WebBaseLoader(url)

docs = loader.load()


print(len(docs))

print(docs[0].page_content)



"""Now we ask some questions."""