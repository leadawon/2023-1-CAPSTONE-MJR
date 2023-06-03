import openai
from .models import menu
# chatgpt.py
# 발급받은 OpenAI API Key 기입
YOUR_API_KEY = ''


def ChatGPT(prompt, API_KEY=YOUR_API_KEY):
    # api key 세팅
    openai.api_key = API_KEY

    # ChatGPT API 호출 및 최신 언어 모델인 text-davinci-003을 가져옴
    completion = openai.Completion.create(
        engine='text-davinci-003'  # 'text-curie-001'  # 'text-babbage-001' #'text-ada-001'
        , prompt=prompt
        , temperature=0.5
        , max_tokens=1024
        , top_p=1
        , frequency_penalty=0
        , presence_penalty=0)

    return completion['choices'][0]['text']

import random

def get_random2(max):
    while True:
        pk = random.randint(1, max)
        if menu.objects.filter(pk=pk).exists():
            return menu.objects.get(pk=pk)

def chatfast(input):
    trigger = f'''
        사용자는 이런 상태입니다. 당신은 긴말필요없이 사용자에게 맞는 음식하나를 말해주세요.
        '''
    what = ChatGPT(input+trigger).strip()
    if menu.objects.filter(category__contains=what).exists():
        food = menu.objects.get(category__contains=what)
    else:
        food = get_random2(1)

    trigger = f'''
    사용자는 이런 상태입니다. 당신은 음식점 이름인 {food.restname}의 {food.foodname}이란 음식을 추천해야 합니다. 가격은 {food.price}원 입니다. 음식점의 위치는{food.location}에 있습니다.
    추천하는 글을 작성해주세요. {food.restname}과 {food.foodname}과 {food.price}는 꼭 들어가야 합니다! 재료에 대한 이야기는 하지말아주세요.
    '''
    return ChatGPT(input+trigger).strip() , input , food.lat, food.lon, food.restname