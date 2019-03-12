import numpy as np
import pandas as pd
from ast import literal_eval
import re

df1 = pd.read_csv('Dataset2.csv')
df2 = pd.read_csv('Dataset3.csv')
pdd = pd.DataFrame(columns=['Usage','Idiom','SenenceNo','Location','Sentence','SentenceBefore','SentenceAfter','SentenceSTEM','SentenceSTEMBefore','SentenceSTEMAfter'])
#POSc5,Pre1C5,Pre2C5,Post1C5,Post2C5,InBetweenC5,NumberOfWords,Bigram, PreBigram
seq = 0
df1['Sentence'] = df1['Sentence'].apply(literal_eval)
def FindIndexes(word, Setnence):
    indexes = []
    index = 0
    for wordd, POS in Setnence:
        if str(wordd) == str(word):
            indexes.append(index)
        index += 1
    return indexes
def DistanceAndWordsBetween(sentence, words, isPOS):
    result = []
    detected = False
    seq = 0
    print(sentence)
    indexes = FindIndexes(words[0] ,sentence)
    print(indexes)
    for index in indexes:
        wordsBetween = []
        num = 0
        for word,POS in sentence:
            if seq < index:
                continue
            seq += 1
            if word == words[0]:
                detected = True
            if word == words[1]:
                detected = False
                break;
            if detected == True:
                if isPOS == True:
                    wordsBetween.append(POS)
                else:
                    wordsBetween.append(word)
                num += 1
        result.append([wordsBetween, num])
    return result

for i in range(0, len(df1)):
    StemmedSentence = pd.DataFrame()
    StemmedSentence = df1.loc[i].values[5]
    #print(StemmedSentence)
    #print(df2.loc[i].values[2],'|||', df1.loc[i].values[5])
    NumberOfWords = len(StemmedSentence)
    VNC = str(df1.loc[i].values[2]).split('_')
    print(df1.loc[i].values[2])
    #print(df1.loc[i].values[5])

    #DistanceAndWordsBetween( StemmedSentence,VNC,False)
    ThereIs = False
    for word, POS in StemmedSentence:
        if VNC[0] == word:
            ThereIs = True
            break;
    if ThereIs == False:
        print(df1.loc[i].values[0] ,'||', StemmedSentence)

    #print(VNC)
    #pdd.loc[seq] = [df1.loc[i].values[1],df1.loc[i].values[2],df1.loc[i].values[3],df1.loc[i].values[4],df1.loc[i].values[5],df1.loc[i].values[6],
    #                df1.loc[i].values[7],df2.loc[i].values[5],df2.loc[i].values[6],df2.loc[i].values[7]]
    seq += 1
print(pdd)