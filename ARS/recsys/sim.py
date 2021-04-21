from nltk.tokenize import RegexpTokenizer, word_tokenize
from nltk.stem import snowball
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

from collections import defaultdict
import json

from gensim.models import doc2vec

def d2v(query_abstract, db_abstract, db_ids):

    #preprocessing query.
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(query_abstract)
    query = [w.lower() for w in tokens]

    #preprocessing db
    db_abstract = [''.join(i) for i in db_abstract]
    db_abstract = [w.lower() for w in db_abstract]
    # db_ids = [i[0] for i in db_ids]
    # db_ids = list(db_ids)
    db = pd.DataFrame.from_records(db_ids, columns =['paper_id'])
    # print(df)
    
    db['abstract'] = db_abstract
    db['abstract'] = db['abstract'].apply(tokenizer.tokenize)
    # print(db)

    class TaggedDocumentIterator(object):
        def __init__(self, doc_list, labels_list):
            self.labels_list = labels_list
            self.doc_list = doc_list
        def __iter__(self):
            for idx, doc in enumerate(self.doc_list):
                yield TaggedDocument(words=doc, tags=[self.labels_list[idx]])
 
    docLabels = list(db['paper_id'])
    data = list(db['abstract'])
    sentences = TaggedDocumentIterator(data, docLabels)

            
    model = Doc2Vec( window=10, min_count=5, workers=11,alpha=0.025)
    model.build_vocab(sentences)
    model.train(sentences,total_examples=model.corpus_count, epochs=model.epochs)

    model.save('model_docsimilarity.doc2vec')
    # Load the model
    model = Doc2Vec.load('model_docsimilarity.doc2vec')

    #### INSTEAD USE COSINE 
    # new_doc_vec = model.infer_vector(query, steps=50, alpha=0.25) /////// inference
    #use the most_similar utility to find the most similar documents.
    # similars = model.docvecs.most_similar(positive=[new_doc_vec])  
    # print(*similars, sep = "\n")
    














    