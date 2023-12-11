import requests
import re
from Providers import Providers
from langchain.llms import Ollama
import torch


def parse_url(url):
    response = requests.get(url)
    html_content =response.content

    print(html_content)
    source = url[0:[m.start() for m in re.finditer(r"/",url)][2]]
    
    with torch.no_grad():
        ollama = Ollama(base_url='http://localhost:11434',
        model="llama2:13b")

    prompt = f'''
html contents:
{html_content}


From the provided html contents of finance website retreive href for the articles about Russian companies and buisness.
Format your answer as numbered list.
Only include the urls in your answer.
    '''


    text_chunk = []

    for chunk in ollama._stream(prompt):
        text_chunk.append(chunk.text)
    print(''.join(text_chunk))


parse_url(url = 'https://www.russia-briefing.com/news/category/business/')
