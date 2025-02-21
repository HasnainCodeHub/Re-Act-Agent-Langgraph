from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from datetime import datetime


import os

load_dotenv(find_dotenv())

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

@tool
def get_current_time_date():
    """Get the current time"""
    print("Getting current time")
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@tool
def hasnain_info():
    """Get the information about Hasnain"""
    print("Getting Hasnain information")
    return """
    Hasnain Ali is a web developer specializing in Next.js, 
    Tailwind CSS, and AI integrations. He has expertise in building chatbots,
    Crew AI, and RAG systems using Google Gemini. He actively contributes to collaborative repositories and maintains a daily project submission streak. 
    He is also Learning Certified Agentic And Robotics  AI Engineer from PIAIC.Find him on GitHub: HasnainCodeHub and LinkedIn: Hasnain Ali."""





agent = create_react_agent(
    llm,
    tools=[get_current_time_date, hasnain_info],
    prompt = 
    """
    You are a helpful assistant that can answer questions and help with tasks.
    you can use the following tools to help you answer questions:
    """
)




def main():
    response = agent.invoke({"messages": "What is Current time? Also provide Hasnain's information"})
    for message in response['messages']:
        message.pretty_print()
        with open("response.txt", "a") as f:
            f.write(message.content)
            print("Response saved to response.txt")

