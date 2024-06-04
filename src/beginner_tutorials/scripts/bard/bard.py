# pip install  google-generativeai
# pip install python-dotenv

import os
import google.generativeai as genai
from dotenv import load_dotenv

def bard_ai_response(question):
    # 加载环境变量文件
    load_dotenv()

    # 获取环境变量值
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

    # 配置 GenerativeAI
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')

    # prompt 设置回答的语气，风格
    prompt = "Just give it to me straight in about 2 sentences,like you're explaining to a friend,like speaching sentence"

    # 生成内容
    response = model.generate_content(f"{prompt}:{question}")
    return response.text


## if main
if __name__ == '__main__':
    question = "What is the meaning of life?"

    response_text = bard_ai_response( question)
    print(response_text)
