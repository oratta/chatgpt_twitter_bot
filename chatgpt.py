import openai
import os
from dotenv import load_dotenv

def get_chatgpt_response(keyword1="", keyword2=""):
    print("start chatgpt")
    load_dotenv()
    openai.api_key = os.getenv('OPENAI_API_KEY')

    # messages = [
    #     {"role": "system", "content": "あなたは10万人のフォロワーを抱える、人気Twitterユーザです。"},
    #     {"role": "user", "content": f"100字以内で{keyword1}と{keyword2}を関連付けて、いいねされそうなツイート文を作成してください."},
    # ]
    messages = [
        {"role": "system", "content": "あなたは臨床心理士として子育て世代のカウンセリングをしています。"},
        {"role": "user", "content": f"280字以内で幼い子供を持つ母親に対して、今日1日を労い、明日も子育てを頑張ろうと思えるようなツイート文を作成してください."},
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    print("end chatgpt")
    return response['choices'][0]['message']['content']
