from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv



load_dotenv()



llm = HuggingFaceEndpoint(
    
    # it represented that which model do you want to use
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)


result = model.invoke("what is the capital of india")

print(result.content)