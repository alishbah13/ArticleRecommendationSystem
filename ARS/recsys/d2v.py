from nltk.tokenize import RegexpTokenizer, word_tokenize
from nltk.stem import snowball

from gensim.models.doc2vec import Doc2Vec, TaggedDocument

from collections import defaultdict
import json

from gensim.models import doc2vec

def d2v(query_abstract, db_abstract):

    #preprocessing query.
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(query_abstract)
    query = [w.lower() for w in tokens]

    #preprocessing db
    db_abstract = [''.join(i) for i in db_abstract]
    for i in db_abstract:
        tokens = tokenizer.tokenize(i)
        db = [w.lower() for w in tokens]


    db = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(db_abstract)]
    max_epochs = 100
    vec_size = 20
    alpha = 0.025

    print(  ' =============== ', db[1])

    model = Doc2Vec(
                    alpha=alpha, 
                    min_alpha=0.00025,
                    min_count=1,
                    dm =1)
    
    model.build_vocab(db)

    for epoch in range(max_epochs):
        print('iteration {0}'.format(epoch))
        model.train(db,
                    total_examples=model.corpus_count,
                    epochs=model.epochs)
        # decrease the learning rate
        model.alpha -= 0.0002
        # fix the learning rate, no decay
        model.min_alpha = model.alpha

    model.save("d2v.model")
    print("Model Saved")

    model= Doc2Vec.load("d2v.model")
    #to find the vector of a document which is not in training data
    # test_data = word_tokenize(query.lower())
    # test_data = query
    v1 = model.infer_vector(query)
    print("V1_infer", v1)

    # to find most similar doc using tags
    similar_doc = model.most_similar('query')
    print(similar_doc)


    # to find vector of doc in training data using tags or in other words, printing the vector of document at index 1 in training data
    # print(model.docvecs['1'])








    