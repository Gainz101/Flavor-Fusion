from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
import pandas as pd
import nltk
from nltk.corpus import stopwords
from gensim.models import Word2Vec

# Import dataset
df = pd.read_csv('all_recipies.csv')

# Create lists of types and descriptions
food_types = df['recipe_name'].tolist()
food_decr_raw = df['description'].tolist()

# Download the stopwords from NLTK
nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

# Function to process each description
def preprocess(description):
    tokens = word_tokenize(description)
    tokens = [word for word in tokens if word.isalnum()]
    postprocessed_desc = [w.lower() for w in tokens if not w.lower() in stop_words]
    return " ".join(postprocessed_desc)

# Preprocess all food descriptions
food_decr = [preprocess(desc) for desc in food_decr_raw]

# Train Word2Vec model
word2vec_model = Word2Vec(sentences=[word_tokenize(desc) for desc in food_decr], vector_size=50, window=5, min_count=1, workers=4)

# Use Word2Vec embeddings to initialize Doc2Vec model
tagged_data = [TaggedDocument(words=word_tokenize(doc.lower()), tags=[str(i)]) for i, doc in enumerate(food_decr)]
doc2vec_model = Doc2Vec(vector_size=50, window=5, min_count=1, workers=4, epochs=100)
doc2vec_model.build_vocab(tagged_data)
doc2vec_model.wv = word2vec_model.wv  # Use Word2Vec embeddings
doc2vec_model.train(tagged_data, total_examples=doc2vec_model.corpus_count, epochs=doc2vec_model.epochs)

# Dining history
dining_history = ["pizza", "salsa", "sandwich", "lasagna", "sushi"]

# Get the document vector for the combined dining history
combined_vector = doc2vec_model.infer_vector(word_tokenize(" ".join(dining_history).lower()))

# Find the most similar food item from the dataset
similar_documents = doc2vec_model.dv.most_similar([combined_vector], topn=1)
similar_food_index = int(similar_documents[0][0])
similar_food = food_types[similar_food_index]

# Print the most similar food item
print(f"The most similar food item to the combined dining history is: {similar_food}")



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