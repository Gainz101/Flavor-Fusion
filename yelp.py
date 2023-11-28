import requests

def search_yelp(api_key, term, location, limit=5):
  
    endpoint = "https://api.yelp.com/v3/businesses/search"

    
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    
    params = {
        "term": term,
        "location": location,
        "limit": limit
    }

  
    response = requests.get(endpoint, headers=headers, params=params)

    
    if response.status_code == 200:
        
        data = response.json()

        
        for business in data.get("businesses", []):
            print(f"Name: {business['name']}")
            print(f"Address: {', '.join(business['location']['display_address'])}")
            print("---")
    else:
        print(f"Error: {response.status_code}, {response.text}")

if __name__ == "__main__":
    
    api_key = "_kpunRxiPhTA4sySgs432sZPBS9afRrsPNYnMOIC66GSuhuadaPuHZfxWiQiu821pjAWVAgJNJ2OEwZjdkbeuphkLzrWEHvWsDFi_gJN7SC-GOn7t6ffJpdWBmFmZXYx"

    
    search_term = "burger"
    location = "College Station, TX"

    
    limit = 5 

    search_yelp(api_key, search_term, location, limit)
