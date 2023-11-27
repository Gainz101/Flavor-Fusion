from bardapi import Bard
import string

# Replace API_KEY with your actual API key
API_KEY = "dQjTcfYZtcqgCTRLrhOWVUcq4zroAWBj7aflgnjdIHviy15ITBhUI0CTCpDQooD3vL4cNQ."

bard = Bard(token=API_KEY)

food = "tacos"
result = bard.get_answer("Give me 5 food places around me related to "+ food )

# Parse the content field
content = result['content']

# Split the content into lines
lines = content.split('\n')

# Filter out the lines that start with '*'
food_places = [line for line in lines if line.startswith('*')]

# Print the food places
for place in food_places:
    print(place)
