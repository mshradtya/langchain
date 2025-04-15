from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

messages = [
    SystemMessage("You are an expert in social media content strategy"),
    HumanMessage("Give a short tip to create engaging posts on Instagram"),
    # we can stack the response, like another AIMessage, followed by a HumanMessage
]

llm = ChatOpenAI(model="gpt-4o")

result = llm.invoke(messages)

print(result.content)