""" Take a example

one pdf

1. send to the model 1
2. generat notes
3. at that same time send to the model 2
4. generate quizes
5. send to the model 3 notes + quizes

6. merze it and display the output"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic # it is for demo you can use in latter a free model bcz of it's a paid model
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel


load_dotenv()

model_1 =  ChatGoogleGenerativeAI(model = "gemini-1.5-flash")

model_2 = ChatAnthropic()


prompt_1 = PromptTemplate(
    template = "Generate short and simple notes from the follwing text \n {text}",
    input_variables = ['text']
)

prompt_2 = PromptTemplate(
    template = "Generate 5 short question answews from the following text \n {text}",
    input_variables = ['text']
)


prompt_3 = PromptTemplate(
    template = "Merge the notes and the quiz into a single document \n notes {notes} and quiz {quiz}",
    input_variables = ['notes','quiz']
)



parser = StrOutputParser()



parallel_chain = RunnableParallel({
    'notes': prompt_1 | model_1 | parser,
    'quiz': prompt_2 | model_2 | parser
})


merge_chain = prompt_3 | model_1 | parser




chain = parallel_chain | merge_chain


text = """“We want you to take from us. We want you, at first, to steal from us, because you
 can’t steal. You will take what we give you and you will put it in your own voice and
 that’s how you will find your voice. And that’s how you begin. And then one day
 someone will steal from you.”
 —Francis Ford Coppola
 At some point, you’ll have to move from imitating your heroes to emulating them. Imitation is about
 copying. Emulation is when imitation goes one step further, breaking through into your own thing.
 “There isn’t a move that’s a new move.” The basketball star Kobe Bryant has admitted that all of his
 moves on the court were stolen from watching tapes of his heroes. But initially, when Bryant stole a
 lot of those moves, he realized he couldn’t completely pull them off because he didn’t have the same
 body type as the guys he was thieving from. He had to adapt the moves to make them his own.
 Conan O’Brien has talked about how comedians try to emulate their heroes, fall short, and end up
 doing their own thing. Johnny Carson tried to be Jack Benny but ended up Johnny Carson. David
 Letterman tried to copy Johnny Carson but ended up David Letterman. And Conan O’Brien tried to be
 David Letterman but ended up Conan O’Brien. In O’Brien’s words, “It is our failure to become our
 perceived ideal that ultimately defines us and makes us unique.” Thank goodness"""


result = chain.invoke({'text': text})


print(result)


# chain.get_graph().print_ascii()