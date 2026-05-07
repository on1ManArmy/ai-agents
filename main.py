from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

llm = ChatGroq(model="llama-3.3-70b-versatile")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    result = agent.invoke({"messages": HumanMessage(
        content="Give me 3 Job search options from linkedin regarding AWS, Nodejs, and AI agets"
    )})
    print(result["messages"][-1].content)

if __name__ == "__main__":
    main()