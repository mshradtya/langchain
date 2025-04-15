from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# load env
load_dotenv()

# create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o")

# define prompt templates
prompt_template = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are a facts expert who knows facts about {animal}.'),
        ('human', 'Tell me {fact_count} facts.'),
    ]
)

# create the combined chain using LangChain Expression Language (LCEL)
chain = prompt_template | model | StrOutputParser() # this function just extracts the content property from the response

# run the chain
result = chain.invoke({"animal": "elephant", "fact_count": 1})

# output
print(result)