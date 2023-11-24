import google_bard

# Replace "YOUR_API_KEY" with the actual API Key obtained earlier
API_KEY = "AIzaSyBqX_7lAyUaAd_bPWhf2OBo8SB-eJnqzYI"

def main():
	query = "What is the meaning of life?"
	response = google_bard.generate_text(query, key=API_KEY)
	print("Google Bard Response (Using google_bard Module):")
	print(response)

if __name__ == "__main__":
	main()

