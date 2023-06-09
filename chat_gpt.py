import openai

openai.api_key = 'your-openai-api-key'

def get_chatgpt_response(keyword):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Tell me about {keyword}."},
        ]
    )

    return response['choices'][0]['message']['content']
