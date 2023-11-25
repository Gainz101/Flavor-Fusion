import google_bard

# Replace "YOUR_API_KEY" with the actual API Key obtained earlier
API_KEY = dQjZqVp3bgmvc_PYzRXDmOfV47vyUClUQW6hS95BF2GT5uNVphCUqqwbl3zQ6M7qJjY5zg

def main():
	query = "What is the meaning of life?"
	response = google_bard.generate_text(query, api_key=API_KEY)
	print("Google Bard Response (Using google_bard Module):")
	print(response)

if __name__ == "__main__":
	main()

