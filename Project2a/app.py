import os
from os import environ as env
from dotenv import load_dotenv
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import OpenAI
#from langchain.chat_models import ChatOpenAI
from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
#import matplotlib.pyplot as plt

 
# Read OpenAI API key from environment variable
#openai_api_key1 = "SSSsk-6TgZRe1vOsNFJmess3WeYcp59Lauggu" 
openai_api_key1 = "ABCsk-sT3zaJOY4nXRXbsbi6692LqE4DuWdtO" 
   
filename="AutoIn.csv"
df = pd.read_csv(filename)

#print(df.to_string())
llm=OpenAI(temperature=0,openai_api_key=openai_api_key1)
agent = create_csv_agent(llm,filename, verbose=True)

question = input("Enter your question: ")
print(question)
result = agent.run(question)

print(result)
 
   
