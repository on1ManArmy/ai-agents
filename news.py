from mcp.server.fastmcp import FastMCP
import uvicorn

mcp = FastMCP("News")

@mcp.tool()
async def get_news(topic: str) -> str:
    """Get latest news headlines about a topic (dummy)."""
    headlines = [
        f"{topic} update 1",
        f"{topic} update 2",
        f"{topic} update 3",
    ]
    return "\n".join(headlines)

if __name__ == "__main__":
    uvicorn.run(app=mcp, host="127.0.0.1", port=8002)
