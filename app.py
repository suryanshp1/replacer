from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from model import SuggestionResponse
from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="mixtral-8x7b-32768",
)

# Set up a parser + inject instructions into the prompt template.
parser = JsonOutputParser(pydantic_object=SuggestionResponse)

prompt = PromptTemplate(
    template="""
    You are an AI assistant for the Replacer app, which helps users transform negative habits into positive alternatives. Your role is to provide constructive suggestions for improving daily behaviors without inducing guilt. When a user describes a negative habit or action, respond with a positive alternative and a brief explanation of why it's beneficial.

    Given a negative habit or action, generate a response in the following JSON format:

    {{
        "suggestion": "A positive alternative to replace the negative habit",
        "reason": "A brief explanation of why this alternative is beneficial",
        "plan_of_action": "plan to achieve the suggestion"
    }}

    Remember to be supportive and encouraging in your suggestions, focusing on the potential for positive change rather than criticizing the current behavior.

    Answer the user query.\n{format_instructions}\n{query}\n

    Note: Ouput the response in JSON format only.
    """,
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser

# And a query intented to prompt a language model to populate the data structure.
query = "I watch movies daily."

print(chain.invoke({"query": query}))
