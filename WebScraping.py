import requests
from bs4 import BeautifulSoup
import re
from Providers import Providers

def parse_url(url, what = '', class_ = '', bad_words = []):
    response = requests.get(url)
    html_content =response.content
    source = url[0:[m.start() for m in re.finditer(r"/",url)][2]]
    soup = BeautifulSoup(html_content, 'html.parser')
    headlines = soup.find_all(what,class_ = class_)
    urls = []
    for headline in headlines:
        out = [headline.text,headline.attrs["href"] if 'href' in headline.attrs else None]
        if (out[1] is None) or (not any(word in out[1] for word in bad_words)):
            urls.append(out)

    return urls

def extract_articles(provider,Providers = Providers):
    out = parse_url(url=Providers[provider].url_main,
                    what =Providers[provider].what_main,
                    class_ = Providers[provider].class_main,
                    bad_words=Providers[provider].bad_words_main)


    texts = []
    l =len(out)
    for i,entry in enumerate(out):
        print(f'{i+1}/{l}  Processing:  ',entry[1])
        out = parse_url(url=entry[1],
                        what =Providers[provider].what_sub,
                        class_ = Providers[provider].class_sub,
                        bad_words=Providers[provider].bad_words_sub)

        texts.append([entry[1],out[0][0]])
    return texts




