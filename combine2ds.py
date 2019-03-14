import numpy as np
import pandas as pd
from ast import literal_eval
from collections import Counter
from senticnet.senticnet import SenticNet
import re

df1 = pd.read_csv('Dataset4.csv')
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

def SentimentsAVGPolarity(sentence):
    sn = SenticNet()
    values = []
    sentence = [stem for word,c5, pos, stem in sentence ]
    for stem in sentence:
        try:
            polarity_value = sn.polarity_intense(stem)
            #print(polarity_value)
            values.append(float(polarity_value))
        except Exception as e:
            #print(stem ,'::', e)
            continue
    if len(values) == 0:
        return 0.0
    return float(sum(values) / len(values))


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
pdd = pd.DataFrame(columns=['Sentence','Usage','Idiom','BetweenPOS','NumOfWordsBetween','PrePOS','prePOS2','postPOS','postPOS2','CountOfSameNounInContext','SentenceLength','SentimentsAVG'])
#                           sentence,usage,idiom,WordsBetween,NumOfWordsBetween,prePOS,prePOS2,postPOS,postPOS2,CountOfSameNounInContext, SentenceLength,sentiments
pdd2 = pd.DataFrame(columns=['SentencePre','Sentence','SentencePost','Idiom','Usage'])
for i in range(0, len(df1)):
    StemmedSentence = pd.DataFrame()
    StemmedSentence = df1.loc[i].values[5]
    StemmedSentencePre = df1.loc[i].values[6]
    StemmedSentencePOST = df1.loc[i].values[7]
    idiom = str(df1.loc[i].values[2])
    usage = str(df1.loc[i].values[1])

    NumberOfWords = len(StemmedSentence)
    VNC = str(df1.loc[i].values[2]).split('_')
    #print(df1.loc[i].values[0])
    #print(df1.loc[i].values[2])
    prePOS = ''
    prePOS2 = ''
    postPOS = ''
    postPOS2 = ''
    WordsBetween = []
    NumOfWordsBetween = 0
    distAndNumber = DistanceAndWordsBetween(StemmedSentence,VNC,False)
    if distAndNumber != None:
        WordsBetween = distAndNumber[0][0]
        NumOfWordsBetween = distAndNumber[0][1]
        prePOS = distAndNumber[0][2]
        prePOS2 = distAndNumber[0][3]
        postPOS = distAndNumber[0][4]
        postPOS2 = distAndNumber[0][5]

    sentence = ' '.join([stem for word,c5,pos,stem in  StemmedSentence])
    sentencePre = ' '.join([stem for word,c5,pos,stem in  StemmedSentencePre])
    sentencePost = ' '.join([stem for word,c5,pos,stem in  StemmedSentencePOST])

    context = ' '.join([stem for word,c5,pos,stem in  StemmedSentence]) + ' '.join([stem for word,c5,pos,stem in  StemmedSentencePre]) + ' '.join([stem for word,c5,pos,stem in  StemmedSentencePOST])
    #CountOfSameNounInContext = context.count(VNC[1])
    SentenceLength = len(StemmedSentence)

    sentiments = SentimentsAVGPolarity(StemmedSentence)
    #Sentence,Usage,Idiom,POSBetween,NumOfWordsBetween,PrePOS,prePOS2,postPOS,postPOS2,CountOfSameNounInContext,SentenceLength,SentimentsAVG
    #pdd.loc[seq] = [sentence,usage,idiom,WordsBetween,NumOfWordsBetween,prePOS,prePOS2,postPOS,postPOS2,CountOfSameNounInContext,
    #                SentenceLength,sentiments]
    pdd2.loc[seq] = [sentencePre,sentence,sentencePost,str(idiom),usage]
    seq += 1
    if seq %10 == 0:
        print(seq)
        pdd2.to_csv('Dataset6.csv')
#print(pdd)