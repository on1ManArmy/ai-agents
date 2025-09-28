import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

def main():
    print("Hello from langchain-course!")
    API_KEY = os.getenv("OPENAI_API_KEY")
    if not API_KEY:
        raise ValueError("OPENAI_API_KEY not found in .env file")

    information = """
    Elon Reeve Musk is an international businessman and entrepreneur known for his leadership of Tesla, SpaceX, X, and the Department of Government Efficiency. Musk has been the wealthiest person in the world since 2021; as of May 2025, Forbes estimates his net worth to be US$424.7 billion
    """
    
    summary_template = """
    Given the information: {information}

    Please provide:
    1. A short summary
    2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], 
        template=summary_template
    )

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    chain = summary_prompt_template | llm
    response = chain.invoke({"information": information})
    
    print("\nResponse from LLM:\n", response.content)

if __name__ == "__main__":
    main()
