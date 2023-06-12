import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_chatgpt_response(keyword1, keyword2):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "あなたは10万人のフォロワーを抱える、人気Twitterユーザです。"},
            {"role": "user", "content": f"100字以内で{keyword1}と{keyword2}を関連付けて、いいねされそうなツイート文を作成してください."},
        ]
    )

    return response['choices'][0]['message']['content']
