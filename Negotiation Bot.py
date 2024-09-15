#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain.schema.output_parser import StrOutputParser
from langchain.schema import AIMessage, HumanMessage,SystemMessage

load_dotenv()
model=ChatOpenAI(model="gpt-3.5-turbo")

prompt_template = ChatPromptTemplate.from_messages()
chat_history = []
name = input("Please Enter Your Name: ")

chat_history.append(HumanMessage(content=f"You are a sales person in a Hyundai car Showroom {name}, state the approximate price of the product and negotiate the price with the buyers offer them max of 10 percentage from the initial price,convince them and seal the deal"))

while True:
    query = input(f"{name}: ")
    if query.lower() == "exit":
        break

    chat_history.append(HumanMessage(content=query))
    chain = prompt_template | model | StrOutputParser()
    result = chain.invoke({"name": name, "chat_history": chat_history})
    response = result
    chat_history.append(AIMessage(content=response))

    print(f"AI {response}")

