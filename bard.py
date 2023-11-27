from bardapi import Bard

# Replace API_KEY with your actual API key
API_KEY = "AIzaSyDGrb8ZtV55BhPq9t35OgBpcTj4bYLHbQ4"

bard = Bard(token=API_KEY)

result = bard.get_answer("Give me 5 food places around me related to tacos?")

# Parse the content field
content = result['content']

# Split the content into lines
lines = content.split('\n')

# Filter out the lines that start with '*'
food_places = [line for line in lines if line.startswith('*')]

# Print the food places
for place in food_places:
    print(place)
