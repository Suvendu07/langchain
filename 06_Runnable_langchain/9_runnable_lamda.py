from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.schema.runnable import RunnablePassthrough, RunnableParallel, RunnableSequence, RunnableLambda


load_dotenv()


def word_count(text):
    return len(text.split())


# runnable_word_count = RunnableLambda(word_count)

# print(runnable_word_count.invoke("Hi there how are you"))


prompt1 = PromptTemplate(
    template = "Generate a joke about {topic}",
    input_variables = ['topic']
)



parser = StrOutputParser()


model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")


joke_gen_chain = RunnableSequence(prompt1, model, parser)


parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_count)
})


final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic':'AI'})


print(result)