from bardapi import Bard

# Replace API_KEY with your actual API key
#API_KEY = "cggGgdKpEjFtDiPxOpUKdP86OMbI9X2_Ufunoho4vXxkXFMxg2WPMjzcaNz_0mDMgIwjHQ."
#API_KEY = "AIzaSyBqX_7lAyUaAd_bPWhf2OBo8SB-eJnqzYI"
API_KEY = "AIzaSyBqX_7lAyUaAd_bPWhf2OBo8SB-eJnqzYI."


bard = Bard(token=API_KEY)

input_query = "What is the capital of France?"
result = bard.retrieve(input_query)
print(result)
