from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated


# Load .env variables (API keys)
load_dotenv()


# Initialize model
model = ChatOpenAI(model="gemini-1.5-flash")


# Define schema using TypedDict
class Review(TypedDict):
    
    """in  this type dict haveing one prob when we pass product_name: str, it's not mean always it returns in str format. sometimes it may be return in int, or any format. if you want to specify some validation like if age > 3 show me but sometime's it may show may be age < 3. so to solve this type of prob use a another method called                  pydantic."""
    
    product_name: Annotated[str,'Give me the product name'] # do same for remaing 
    rating: float
    pros: str
    cons: str
    overall_review: str


# Wrap the model with structured output schema
str_model = model.with_structured_output(Review)  # Pass the class, not a dict




# Example input text
review_text = (
    "I recently bought the Noise Cancelling Headphones. The sound quality is crystal clear "
    "and the noise cancellation works amazingly well in noisy areas. The battery lasted me around "
    "25 hours, which is pretty good. They are very comfortable, though after 3 hours of use, my ears felt a bit warm. "
    "I’d rate them 4.5 out of 5. Overall, worth the money!"
)


# Invoke the structured model
result = str_model.invoke(review_text)


# Print the structured output
print(result)


# this code is not for run bcz of no API call