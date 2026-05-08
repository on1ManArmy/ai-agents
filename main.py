from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage

MAX_ITERATIONS = 10
MODEL = "quen3:1.7b"

# tools
@tool
def get_product_price(product: str) -> float:
    """Lookup the price of a product by its name in catalog"""
    prices = {"laptop": 1299.99, "headphones": 149.5, "keyword": 89.50}
    return prices[product]

@tool
def apply_discount(price: float, discount_tier: str) -> float:
    """Apply discount to price
    Available tiers are: bronze, silver, gold"""
    discount_percentages = {"bronze": 5, "silver": 10, "gold": 20}
    discount = discount_percentages[discount_tier]
    return round(price * (1 - discount/100), 2)

# agents loop
def run_agent(question: str):
    pass

def main():
    print("Welcome to LangChain! (.bind_tools)")
    result = run_agent("What is the price of laptop after applying gold discount?")
    print(result)

if __name__ == "__main__":
    main()