import tensorflow as tf
from gensim.models import KeyedVectors

import skip_thoughts

# Initialize the word2vec and skip-thoughts models only once:
word2vec_model = KeyedVectors.load('E:/Data/GoogleNews-vectors-negative300.bin.gz', mmap='r')
graph = tf.Graph()
with graph.as_default():
    # Refer to the constructor docstring for more information on the arguments.
    model = skip_thoughts.SkipThoughts(word2vec_model, **kwargs)

with tf.Session(graph=graph):
    # Restore the model only once.
    # Here, `save_dir` is the directory where the .ckpt files live. Typically
    # this would be "output/mymodel" where --model_name=mymodel in train.py.
    model.restore('')

    # Run the model like this as many times as desired.
    print(model.encode(['asdas dasdasda skjaksdask', 'asdas kjhare tretrete']))
