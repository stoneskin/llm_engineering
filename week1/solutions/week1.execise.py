import os
import requests
import json
from typing import List
from dotenv import load_dotenv
from bs4 import BeautifulSoup
#from IPython.display import Markdown, display, update_display
from openai import OpenAI


load_dotenv(override=True)
api_key = os.getenv('Open_Router_Key')

if api_key and api_key.startswith('sk-or-v1') and len(api_key)>10:
   print("API key looks good so far")
else:
   print("There might be a problem with your API key? Please visit the troubleshooting notebook!")
    
#MODEL = 'gpt-4o-mini'
#openai = OpenAI()

#MODEL = 'deepseek-r1:1.5b'
#openai = OpenAI(
#    base_url="http://localhost:11434/v1",
#    api_key="ollama"
#)
MODEL = 'google/gemini-2.0-flash-lite-preview-02-05:free'
MODEL = 'google/gemini-2.0-flash-thinking-exp:free'
MODEL ='google/gemini-2.0-pro-exp-02-05:free'
#MODEL ='qwen/qwen2.5-vl-72b-instruct:free'
#MODEL ='deepseek/deepseek-r1-distill-llama-70b:free'

openai = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

question = """
Please explain what this code does and why:
yield from {book.get("author") for book in books if book.get("author")}
"""

question = input("Please enter your question:")

system_prompt = "You are a helpful technical tutor who answers questions about python code, software engineering, data science and LLMs"
user_prompt = "Please give a detailed explanation to the following question: " + question


messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

response = openai.chat.completions.create(
        model=MODEL,
        messages=messages
    )

answer=response.choices[0].message.content
print(answer)
#display(Markdown(answer))