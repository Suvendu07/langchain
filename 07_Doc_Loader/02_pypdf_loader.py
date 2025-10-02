"""It give in page by page

like if there is a pdf having 25 page. it give 25 doc. obj.
means after processing it give a list of 25 object's"""


from langchain_community.document_loaders import PyPDFLoader


loder = PyPDFLoader('D:\LangChain\Pdf of langchain\LangChain_Prompts_Explanation.pdf')


docs = loder.load()

print(docs)

print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)


"""It is use in when most of are text.
if these is in img it not working well."""