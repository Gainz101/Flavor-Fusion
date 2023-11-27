from gensim.models.doc2vec import Doc2Vec,\
TaggedDocument

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from sklearn.metrics.pairwise import cosine_similarity

import numpy as np
import re
import csv
import pandas as pd
from spellchecker import SpellChecker  # Import the SpellChecker

# Importants dataset 
df = pd.read_csv('all_recipies.csv')

# Creates 2 seperate 'list' w/ types and decription
food_types = df['recipe_name'].tolist()
food_decr_raw = df['description'].tolist()


### Need to clean the food decriptions
## remove stopwords, remove punctuations, convert to lowercase

# Download the stopwords from NLTK
# nltk.download('punkt')
# nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

# function to proccess each decription
def preproccess(decription):
    # Tokenize the text
    tokens = word_tokenize(decription)

    # Remove punctuations
    tokens = [word for word in tokens if word.isalnum()]

    # Convert lowercase and remove stop words
    postprocess_decr = [w.lower() for w in tokens if not w.lower() in stop_words]

    # remake decription
    return " ".join(postprocess_decr)

# Utilize function above (^) in order to convert all of food decription
food_decr = []
for i in range(0, len(food_decr_raw)):
    proc_decr = preproccess(food_decr_raw[i])
    # also add the respected food_type to begging of food_decr (adds more emphasis on food_type)
    proc_decr = str(food_types[i]).lower() + " " + proc_decr
    
    # add to list
    food_decr.append(proc_decr)

tagged_data = [TaggedDocument(words=word_tokenize(doc.lower()),
                              tags=[str(i)]) for i,
               doc in enumerate(food_decr)]

# train the Doc2vec model
model = Doc2Vec(vector_size=20,
                min_count=2, epochs=50)

model.build_vocab(tagged_data)

model.train(tagged_data,
            total_examples=model.corpus_count,
            epochs=model.epochs)
 
# get the document vectors
document_vectors = [model.infer_vector(
    word_tokenize(doc.lower())) for doc in proc_decr]
 
#  print the document vectors
for i in range(0, 3):
    print("Document", food_types[i], ":", proc_decr[i])
    print("Vector:", document_vectors[i])
    print()

# # define a list of documents.
# data = ["This is the first document",
#         "This is the second document",
#         "This is the third document",
#         "This is the fourth document"]
 
# preproces the documents, and create TaggedDocuments
# tagged_data = [TaggedDocument(words=word_tokenize(doc.lower()),
#                               tags=[str(i)]) for i,
#                doc in enumerate(data)]
 
# # train the Doc2vec model
# model = Doc2Vec(vector_size=20,
#                 min_count=2, epochs=50)
# model.build_vocab(tagged_data)
# model.train(tagged_data,
#             total_examples=model.corpus_count,
#             epochs=model.epochs)
 
# # get the document vectors
# document_vectors = [model.infer_vector(
#     word_tokenize(doc.lower())) for doc in data]
 
# #  print the document vectors
# for i, doc in enumerate(data):
#     print("Document", i+1, ":", doc)
#     print("Vector:", document_vectors[i])
#     print()


#Bard - Searching for restaurants nearby 
'''
# Replace API_KEY with your actual API key
API_KEY = "dQjTcZCzYfXtNEZCvwPVpWvIFkmCZvtyFF_jsoi0R45nP54lYKKJVLKMvtonqYLhzhD0Rg."

bard = Bard(token=API_KEY)

result = bard.get_answer("Give me 5 food places around me related to " + recommended_dish)

# Parse the content field
content = result['content']

# Split the content into lines
lines = content.split('\n')

# Filter out the lines that start with '*'
food_places = [line for line in lines if line.startswith('*')]

# Print the food places
for place in food_places:
    print(place)
'''