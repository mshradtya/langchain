from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# load env
load_dotenv()

# create a ChatOpenAI model
model = ChatOpenAI(model='gpt-4o')

chat_history = [] # use a list to store messages

# set an initial system message ( optional )
system_message = SystemMessage(content='You are a helpful AI assistant.')
chat_history.append(system_message) # add system message to chat history

# chat loop
while True:
    query = input("You: ")
    if (query.lower() == 'exit'):
        break
    chat_history.append(HumanMessage(content=query)) # add user message

    # get AI response using history
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response)) # add AI message

    print(f"AI: {response}")

print("--- Message History ---")
print(chat_history)