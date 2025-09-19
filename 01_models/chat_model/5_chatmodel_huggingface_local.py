from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline


# this line for dw in a specific path. while bydefault it dw in c drive
import os
os.environ['HF_HOME'] = "D:/huggingface_cache"


llm = HuggingFacePipeline.from_model_id(
        repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        task = "text-generation",
        
        pipeline_kwargs = dict(
            temperature = 0.5,
            max_new_token = 10
        )
)

model = ChatHuggingFace(llm = llm)

result = model.invoke("what is the capital of india")

print(result.content)


""" when we run this code it download the tinyllama model and all 
the confugaration as we provide with us. i think it may be around 500MB."""


# so that i can't run this code