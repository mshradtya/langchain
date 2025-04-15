from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4")

# template = "Write a {tone} email to {company} expressing interest in the {position} " \
# "mentioning {skill} as a key strength. Keep it 4 lines max."

# # converting the template to prompt template, that langchain will understand
# prompt_template = ChatPromptTemplate.from_template(template)

# # replacing placeholders with actual values
# prompt = prompt_template.invoke({
#     "tone": "energetic",
#     "company": "Samsung",
#     "position": "AI Engineer",
#     "skill": "AI"
# })

# example 2: prompt with system and human messages
messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes."),
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})
result = llm.invoke(prompt)

print(result.content)