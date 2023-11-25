from bardapi import Bard

# Replace API_KEY with your actual API key
API_KEY = "dQjZqQzR9M6HH_KhYMoag7vDze3qTkG_nizXGID8HuRPEU2IqX-bXks9SqlB1DMnzGaudA."

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
