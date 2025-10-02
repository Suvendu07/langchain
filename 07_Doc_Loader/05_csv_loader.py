from langchain_community.document_loaders import CSVLoader

# Use a safer encoding like 'utf-8' or 'latin1' depending on your file's content
loader = CSVLoader(
    file_path="C:/Users/Suvendu Khuntia/Downloads/combined_text_data.csv",
    encoding="utf-8-sig"
)

docs = loader.load()

print(f"Loaded {len(docs)} documents.")

# Optional: Preview the first document
print(docs[0] if docs else "No documents loaded.")
