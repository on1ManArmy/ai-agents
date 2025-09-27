import os
from dotenv import load_dotenv

load_dotenv()

def main():
    print("Hello from langchain-course!")
    API_KEY = os.getenv("OPENAI_API_KEY")
    print("Api Key is: ", API_KEY)

if __name__ == "__main__":
    main()
