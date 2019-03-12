import numpy as np
import pandas as pd
from ast import literal_eval
from collections import Counter

import re

df1 = pd.read_csv('Dataset4.csv')
pdd = pd.DataFrame(columns=['Usage','Idiom','SenenceNo','Location','Sentence','SentenceBefore','SentenceAfter','SentenceSTEM','SentenceSTEMBefore','SentenceSTEMAfter'])
#POSc5,Pre1C5,Pre2C5,Post1C5,Post2C5,InBetweenC5,NumberOfWords,Bigram, PreBigram
seq = 0
df1['Sentence'] = df1['Sentence'].apply(literal_eval)
df1['SentenceBefore'] = df1['SentenceBefore'].apply(literal_eval)
df1['SentenceAfter'] = df1['SentenceAfter'].apply(literal_eval)

def FindIndexes(word, Setnence):
    indexes = []
    index = 0
    for wordd, c5, pos, stem  in Setnence:
        if stem == word:
            indexes.append(index)
        index += 1
    return indexes


def DistanceAndWordsBetween(sentence, words, isPOS):
    result = []
    indexes = FindIndexes(words[0] ,sentence)

    stems = [word for wordFull, c5, pos, word in sentence]
    word2 = words[1]
    posPre = ''
    posPre2 = ''
    posPost = ''
    posPost2 = ''
    index = 0
    if len(indexes) == 0:
        return None
    if (len(indexes) > 1):
        distances = []
        for index in indexes:
            distance = 0
            for i in range(index, len(stems) - 1):
                if stems[i] == word2:
                    break;
                else:
                    distance += 1
            distances.append([index, distance])
        index = min(distances, key=lambda t: t[1])[0]
    else:
        index = indexes[0]
    wordsBetween = []
    if (index != 0):
        posPre = sentence[index - 1][1]
    if (index - 1 != 0):
        posPre2 = sentence[index - 2][1]
    for i in range(index + 1,len(stems) - 1):
        if stems[i] == word2:
            if (i + 1 <= len(stems) - 1):
                posPost = sentence[i + 1][1]
            if (i + 2 <= len(stems) - 1):
                posPost2 = sentence[i + 2][1]
            break;
        else:
            wordsBetween.append(sentence[i][1])
    result.append([wordsBetween,len(wordsBetween),posPre,posPre2,posPost,posPost2])
    return result
for i in range(0, len(df1)):
    StemmedSentence = pd.DataFrame()
    StemmedSentence = df1.loc[i].values[5]
    StemmedSentencePre = df1.loc[i].values[6]
    StemmedSentencePOST = df1.loc[i].values[7]

    NumberOfWords = len(StemmedSentence)
    VNC = str(df1.loc[i].values[2]).split('_')
    #print(df1.loc[i].values[0])
    #print(df1.loc[i].values[2])

    distAndNumber = DistanceAndWordsBetween(StemmedSentence,VNC,False)
    #if distAndNumber != None:
    #    print(distAndNumber[0][3])

    context = ' '.join([stem for word,c5,pos,stem in  StemmedSentence]) + ' '.join([stem for word,c5,pos,stem in  StemmedSentencePre]) + ' '.join([stem for word,c5,pos,stem in  StemmedSentencePOST])
    count = context.count(VNC[1])
    SentenceLength = len(StemmedSentence)
    #counter = Counter(context)
    #if (counter[VNC[1]] != 0):
    #    print(counter[VNC[1]])
    #print(VNC)
    #pdd.loc[seq] = [df1.loc[i].values[1],df1.loc[i].values[2],df1.loc[i].values[3],df1.loc[i].values[4],df1.loc[i].values[5],df1.loc[i].values[6],
    #                df1.loc[i].values[7],df2.loc[i].values[5],df2.loc[i].values[6],df2.loc[i].values[7]]
    seq += 1
print(pdd)