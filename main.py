from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from googlesearch import search
import re
import csv

# Example data (replace with your actual data)
# diningHistory = [
#     "I love sushi and pasta.",
#     "pizza is my favorite.",
#     "sushi and sushi are delicious.",
#     "I ate pizza the other day.",
#     "i usually have oatmeal at around 10",
#     "i love oatmeal",
#     "i love oatmeal",
#     # ...
# ]


diningHistory=[]

print("---------------------------------------\nWelcome to FlavorFusion!!\n---------------------------------------")
# print("How many people will you be dining with? ")
# num_users = input()

print("Enter 5 food you've ate recentely or that you like: ") 
for i in range(0,5):
    diningHistory.append(input())


# Tokenize and preprocess the data
# tokenized_corpus = [word_tokenize(sentence.lower()) for sentence in diningHistory]
tokenized_corpus = [sentence.lower().split() for sentence in diningHistory]


# Train Word2Vec model
model = Word2Vec(sentences=tokenized_corpus, vector_size=100, window=5, min_count=1, workers=4)

IN_embs = model.wv
OUT_embs = model.syn1neg

##Data Creation done
#####################################################################################################################################

def create_user_profile(user_reviews, model):
    # Convert user reviews to lowercase and tokenize
    tokenized_reviews = [review.lower().split() for review in user_reviews]

    # Get embeddings for words in the vocabulary
    embeddings = [IN_embs[word] for review in tokenized_reviews for word in review if word in IN_embs]

    if not embeddings:
        return np.zeros(model.vector_size)  # Return zero vector if no valid embeddings

    return np.mean(embeddings, axis=0)


# Example user reviews
# user_reviews = ["I enjoyed pasta yesterday.", "Sushi is always a good choice."]

# Create user profile vector
user_profile = create_user_profile(diningHistory, model)

# Compare user profile with different food types
# food_types = ["pizza", "sushi", "burger", "pasta", "salad", "ice_cream","oatmeal"]

### Puts all food items into array 
food_types = []
# reads all csv file that contains 426,740 types of food 
with open('dish.csv', 'r', encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header
    food_types = [row[1] for row in reader]  # Indexing starts at 0

        

#print(food_type[2])
# Compare user profile with different food types
similarities = []

for food in food_types:
    if food in IN_embs:
        similarity = cosine_similarity([user_profile], [IN_embs[food]])[0][0]
    else:
        similarity = 0
    similarities.append(similarity)

# The outputs of the similarity are parrallel to the food_types
# Meaning that if you don't list a specific food_types in the dataset it will output 0
# Issue: It can't draw a sufficient conclusion if you don't list the food item in food_types

recommended_food = food_types[np.argmax(similarities)] #Recommend the food type with the highest cosine similarity

# for word in IN_embs.index_to_key:
#     print(word, IN_embs[word])


print("Recommended food type:", recommended_food)

# # Start of Python file

# # Create a list of food items
# foods = ["Pizza", "Burger", "Pasta", "Sushi", "Tacos", "Salad", "Steak", "Ice Cream", "Donuts", "Fries"]

# # Create an empty list to store the ratings
# ratings = []

# # Ask the user to rate each food
# for food in foods:
#     while True:
#         try:
#             rating = int(input(f"On a scale of 1-10, how much do you like {food}? "))
#             if 1 <= rating <= 10:
#                 ratings.append(rating)
#                 break
#             else:
#                 print("Invalid input. Please enter a number between 1 and 10.")
#         except ValueError:
#             print("Invalid input. Please enter a number.")

# # Print out the ratings
# print("Your food ratings are:", ratings)

# # End of Python file
