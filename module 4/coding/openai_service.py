import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def call_open_ai(question):
    client = OpenAI()
    response = client.chat.completions.create(
        temperature=0,
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":"you are a chat bot answer questions based on the given data"},
            {"role":"user","content": question}
        ]
    )
    print(response)
    return response.choices[0].message.content


answer = call_open_ai("how are you")
print(answer)