from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()

while True:
    user_input = input("Enter your question: ")
    if user_input == "exit":
        print("Exiting the chatbot. Goodbye!")
        break

    response = model.invoke(user_input)
    print("Ai response:", response.content)