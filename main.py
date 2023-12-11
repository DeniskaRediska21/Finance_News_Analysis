from langchain.llms import Ollama
import torch
import WebScraping


with torch.no_grad():
    ollama = Ollama(base_url='http://localhost:11434',
    model="mistral")


scrape = WebScraping.extract_articles(provider = 'russia-briefing')
l = len(scrape)
for i,news in enumerate(scrape):
    prompt = f'''Analise the news: {news[1]}

    In your responce you should answer to the questions:
    1)What is the company in question?
    2)How this news will effect the stock price of the company?

    Answer to the first question should be one word, should only consist of the name of the company.
    Answer to the second question should only consist of: 'Rise', 'Fall' or 'I don't know'
    Answer in form:
        1) Answer to the first question
        2) Answer to the second question
    '''


    text_chunk = []

    for chunk in ollama._stream(prompt):
        text_chunk.append(chunk.text)


    print(f'{i+1}/{l}   From:  ',news[0])
    print(''.join(text_chunk))
