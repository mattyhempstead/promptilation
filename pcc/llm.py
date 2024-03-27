from dotenv import load_dotenv
load_dotenv()

import os
from openai import OpenAI

client = OpenAI()

GPT_MODEL = "gpt-3.5-turbo-1106"


def get_chat_response(
    system_message: str,
    user_request: str,
    seed: int = None,
    temperature: float = 0.7
):

#     return """
# MOCK MESSAGE
# ```
# print("Hello, World!")
# ```
#     """

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_request},
    ]

    response = client.chat.completions.create(
        model=GPT_MODEL,
        messages=messages,
        seed=seed,
        max_tokens=200,
        temperature=temperature,
    )

    response_content = response.choices[0].message.content
    system_fingerprint = response.system_fingerprint
    prompt_tokens = response.usage.prompt_tokens
    completion_tokens = response.usage.total_tokens - response.usage.prompt_tokens

    print(f"""
    Response: {response_content}
    System Fingerprint: {system_fingerprint}
    Number of prompt tokens: {prompt_tokens}
    Number of completion tokens: {completion_tokens}
    """)

    return response_content
