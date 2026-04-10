import requests
from bs4 import BeautifulSoup

url="https://www.zaubacorp.com/companysearchresults/CHENNAI"
requests_1=requests.get(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"})
soup=BeautifulSoup(requests_1.content, "html.parser")

rows=soup.find_all("tr")

#import nltk
#nltk.download("punkt_tab")
#tokens=nltk.word_tokenise(str)
#nltk.download("averaged_perceptron_tagger_eng")
#tagged=nltk.pos_tag(tokens)
#nltk.download("maxent_ne_chunker_tab")
#nltk.download("words")
#pip install svgling
#ner_chunk=nltk.ne_chunk(tagged)
#ner_chunk[0].label()
#for chunk in ner_chunk:
#if hasattr(chunk,"label"):
#print(chunk.label()," ".join(c[0] for c in chunk))
#set(words.words())
#corrected_text=[]
#for word in word token:
#if word.lower() not in english_words and word.isaplha():
##suggestions=[]
#for w in english_words:
#if nltk.edit_distance(word,w)==1:
#suggestions.append(w)
#break
#if suggestions:
#corrected_text.append(suggestions[0])
#else:
#corrected_text.append(word)
#else:
#corrected_text.append(word)
#print(" ".join(corrected_text))