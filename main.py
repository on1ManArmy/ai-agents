from dotenv import load_dotenv
load_dotenv()
from typing import List
from pydantic import BaseModel, Field
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

class Source(BaseModel):
    """Scheme for source used by agent"""
    url: str = Field(description="Source URL")

class AgentResponse(BaseModel):
    """Scheme for response to agent"""
    answer: str = Field(description="Response to agent")
    sources: List = Field(default_factory=list, description="List of sources used by agent")

llm = ChatGroq(model="llama-3.3-70b-versatile")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    result = agent.invoke({"messages": HumanMessage(
        content="Give me 3 Job search options from linkedin regarding AWS, Nodejs, and AI agets"
    )})
    print(result["messages"][-1].content)

if __name__ == "__main__":
    main()