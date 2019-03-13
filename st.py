import numpy
import pandas as pd
from skip_thoughts import configuration
from skip_thoughts import encoder_manager
import os

FLAGS = {}
FLAGS['logdir'] = ''

f = open('ckpt/model.ckpt-9999.index')

df = pd.read_csv('Dataset5.csv')
sentences = df.values[1]
manager = encoder_manager.EncoderManager()
checkpoint_path = os.path.join('ckpt', "model.ckpt-9999")
folder = 'd:/skip_thoughts_uni_2017_02_02/skip_thoughts_uni_2017_02_02/'
manager.load_model(configuration.model_config(), folder+'vocab.txt', folder+'embeddings.npy',checkpoint_path=folder+'model.ckpt-501424')
encodings = manager.encode(sentences)