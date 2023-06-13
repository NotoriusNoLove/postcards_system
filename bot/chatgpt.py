import openai
# TODO: api_key to .env
openai.api_key = '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'

messages = [
    {
        "role": "system", "content": """You're a kind helpful assistant 
    who needs to write a birthday greeting!"""
    }
]


def chatgpt(content: str):
    messages.append({"role": "user", "content": content})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5,
        max_tokens=50,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    chat_response = completion.choices[0].message.content
    return chat_response


if __name__ == "__main__":
    print(chatgpt("Напиши как дела"))
