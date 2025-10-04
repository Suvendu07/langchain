from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """aksdjha skashdkajs kahdska sdhdfhjsd wmhegwe dksadhg ,jcd qwejrgjbjwgewegjg djasgdghagd gahscjasgfdhjgas fvdg asfdhtartfwteqhgjhgxdgfshgafdgfasfkdjqwteytq wxhjwq hggqwfehgqw
asdghjasgdhjad ajdgjqwgjegqwhjqwegeri jdhfgjsgdefjasGEHGREGWRG JAEDJCGEJGDGED AJHSDGJASHGDHJAGSUhjhsdhjhgfhjsegruywegrjcjqwyeruwqgtryuw suvcendfuy kynt ais a sgiif but in asdguasdgjadg """


spiltter = RecursiveCharacterTextSplitter(
    chunk_size = 10,
    chunk_overlap = 0
)

result = spiltter.split_text(text)


print(len(result))
print(result)