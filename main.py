from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from tavily import TavilyClient

tavily = TavilyClient()

@tool
def search(query: str) -> dict:
    """
    Tool that searches over internet
    Args:
        query: The search query for internet
    Returns:
        The search result
    """
    print("Searching for {}".format(query))
    return tavily.search(query)

llm = ChatGroq(model="llama-3.1-8b-instant")
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    result = agent.invoke({"messages": HumanMessage(
        content="What is weather in Hyderabad only today temprature?"
    )})
    print(result["messages"][-1].content)

if __name__ == "__main__":
    main()