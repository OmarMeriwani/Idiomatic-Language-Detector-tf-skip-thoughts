import numpy as np
import pandas as pd
import xml.etree.ElementTree
from bs4 import BeautifulSoup
from nltk.corpus.reader.bnc import BNCCorpusReader
from nltk.corpus.reader.bnc import BNCSentence

from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder
from collections import namedtuple
import xml.etree.ElementTree as ET
print('Read CSV.')
df = pd.read_csv('VNC-Tokens.csv', header=0)
original_path = 'D:/British National Corpus/2554/download/Texts/'
'''fileids = []
print('Setting values to array.')
for i in df.values:
    fileids.append(i[2] + '.xml')
'''
dfo = pd.DataFrame(columns=['Usage','Idiom','SenenceNo','Location','Sentence','SentenceBefore','SentenceAfter'])
seq = 0
for i in df.values[:5]:
    fileid=  i[2] + '.xml'
    bnc_reader = BNCCorpusReader(root=original_path, fileids=fileid)
    try:
        dfo.loc[seq] =[i[0],i[1],i[3],i[2], bnc_reader.tagged_sents()[i[3]-1],bnc_reader.tagged_sents()[i[3]-2],bnc_reader.tagged_sents()[i[3]]]
    except:
        continue
    seq += 1
    if seq % 10 == 0:
        print(seq)
        #dfo.to_csv('Dataset3.csv')
    #print(i[0],'|',i[1],'|',i[3],'|',i[2],'|', bnc_reader.tagged_sents()[i[3]-1],bnc_reader.tagged_sents()[i[3]-2],bnc_reader.tagged_sents()[i[3]])
print(len(dfo))
#print(sorted_bigrams)

'''
df = df[:1]
for i in df.values:
    newPath = original_path + i[2] + '.xml'
    tt = nltk.corpus.reader.bnc.BNCCorpusReader(newPath,fileids=1)
    print(tt)
    e = xml.etree.ElementTree.parse(newPath)
    for i in e.getiterator('wtext'):
        print(i[5])
        for j in i[5]:
            for k in j:
                print(str(k))'''
