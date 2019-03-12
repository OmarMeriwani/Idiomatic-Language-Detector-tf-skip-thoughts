import numpy as np
import pandas as pd
import xml.etree.ElementTree
from bs4 import BeautifulSoup

print('Read CSV.')
df = pd.read_csv('VNC-Tokens.csv', header=0)
original_path = 'D:/British National Corpus/2554/download/Texts/'
dfo = pd.DataFrame(columns=['Usage','Idiom','SenenceNo','Location','Sentence','SentenceBefore','SentenceAfter'])
seq = 0
for i in df.values:
    fileid=  i[2] + '.xml'
    n = open(original_path + fileid)
    text = n.read()
    soup = BeautifulSoup(text)
    n_sent = str(i[3])
    n_sent_pre = str(i[3] - 1)
    n_sent_post = str(i[3] + 1)
    sent = soup.find('s',{'n': n_sent})
    sent_pre = soup.find('s',{'n': n_sent_pre})
    sent_post = soup.find('s',{'n': n_sent_post})

    soup = BeautifulSoup(str(sent))
    words = soup.find_all('w')
    sent_words = []
    for word in words:
        soup = BeautifulSoup(str(word))
        sent_words.append([word.text, word['c5'], word['pos'], word['hw']])

    soup = BeautifulSoup(str(sent_pre))
    words = soup.find_all('w')
    sent_pre_words = []
    for word in words:
        soup = BeautifulSoup(str(word))
        sent_pre_words.append([word.text, word['c5'], word['pos'], word['hw']])

    soup = BeautifulSoup(str(sent_post))
    words = soup.find_all('w')
    sent_post_words = []
    for word in words:
        soup = BeautifulSoup(str(word))
        sent_post_words.append([word.text, word['c5'], word['pos'], word['hw']])

    try:
        dfo.loc[seq] =[i[0],i[1],i[3],i[2], sent_words,sent_pre_words,sent_post_words]
    except:
        continue
    seq += 1
    if seq % 10 == 0:
        print(seq)
        dfo.to_csv('Dataset4.csv')