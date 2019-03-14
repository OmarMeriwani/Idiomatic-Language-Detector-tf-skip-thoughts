import numpy
import pandas as pd
from skip_thoughts import configuration
from skip_thoughts import encoder_manager
import os

FLAGS = {}
FLAGS['logdir'] = ''

df = pd.read_csv('Dataset6.csv')
sentences = df.values[1]
manager = encoder_manager.EncoderManager()
folder = 'd:/skip_thoughts_uni_2017_02_02/skip_thoughts_uni_2017_02_02/'
manager.load_model(configuration.model_config(), folder+'vocab.txt', folder+'embeddings.npy',checkpoint_path=folder+'model.ckpt-501424')
pd = pd.DataFrame(columns=['vector','idiom','usage'])
#df = df[:10]
seq = 0
for i in range(0, len(df)):
    enco =[]
    try:
        encodings = manager.encode([df.loc[i].values[1],df.loc[i].values[2],df.loc[i].values[3]])
        for e in encodings[1]:
            enco.append(e)
        print(seq, encodings[1])
        #enco = encodings[1]
    except:
        continue
    pd.loc[seq] = [enco,df.loc[i].values[4],df.loc[i].values[5]]
    seq += 1
pd.to_csv('Dataset-Skip-Thoughts.csv')