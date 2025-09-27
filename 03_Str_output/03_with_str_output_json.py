# langchain_review.py

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field

# Load API key from .env
load_dotenv()


# Initialize LLM model
# Replace "gemini-1.5-flash" with your model if needed
model = ChatOpenAI(model="gemini-1.5-flash")


# Define structured schema using Pydantic

json_schema = {
    "title": "student",
    "description": "schema about student",
    "type": "object",
    "properties": {
        "name" : "String",
        "age" : "integer"
    },

    "required": ["name"]
}

# Wrap the LLM with structured output schema
str_model = model.with_structured_output(json_schema)


# Example input review text
review_text = (
    "I recently bought the Noise Cancelling Headphones. The sound quality is crystal clear "
    "and the noise cancellation works amazingly well in noisy areas. The battery lasted me around "
    "25 hours, which is pretty good. They are very comfortable, though after 3 hours of use, my ears felt a bit warm. "
    "I’d rate them 4.5 out of 5. Overall, worth the money!"
)


# Invoke the structured model (makes the API call)
result = str_model.invoke(review_text)


# Access individual fields
print("Product Name:", result.product_name)
print("Rating:", result.rating)
print("Pros:", result.pros)
print("Cons:", result.cons)
print("Overall Review:", result.overall_review)

# Or print full JSON
print("\nStructured Output (JSON):")
print(result.json(indent=2))
