"""
API Fundamentals and Best Practices:

1. Making API Calls:
   - APIs (Application Programming Interfaces) are endpoints that allow systems to communicate
   - Common HTTP methods:
     * GET: Retrieve data (like this example)
     * POST: Create new data
     * PUT/PATCH: Update existing data
     * DELETE: Remove data
   - URLs usually consist of:
     * Base URL (e.g., https://api.freeapi.app)
     * Endpoint path (e.g., /api/v1/public/randomusers)
     * Query parameters (e.g., ?page=1&limit=10)

2. Authentication Methods:
   - API Key: A simple token added to headers or query parameters
     headers = {'X-API-Key': 'your_api_key_here'}
   - Bearer Token: Usually for OAuth/JWT
     headers = {'Authorization': 'Bearer your_token_here'}
   - Basic Auth: Username/password encoded
     auth = ('username', 'password')
   - No Auth: Some public APIs (like this one) don't require authentication

3. Error Handling Best Practices:
   - Always check HTTP status codes (200s: success, 400s: client errors, 500s: server errors)
   - Handle network errors (connection timeout, DNS failures)
   - Validate API response format
   - Implement retry logic for transient failures
   - Log errors for debugging

4. Working with JSON:
   - JSON is a common API data format
   - response.json() converts JSON string to Python dictionary
   - Use dict.get() for safe access to nested data
   - Always validate data structure before accessing
   - Handle missing or null values gracefully
"""

import requests

def fetch_data_from_api():
    # 1. Making the API call
    url = "https://api.freeapi.app/api/v1/public/randomusers"
    
    # You can add authentication if required:
    # headers = {'Authorization': 'Bearer your_token'}
    # response = requests.get(url, headers=headers)
    
    # Making GET request to the API
    response = requests.get(url)
    
    # Error handling: Check status code
    response.raise_for_status()  # Raises HTTPError for bad status codes
    
    # Parse JSON response
    data = response.json()

    # Validate response structure and extract data
    if data["success"] and "data" in data and "data" in data["data"]:
        # Safely extract nested data
        user_data = data["data"]["data"][0]
        username = user_data["login"]["username"]
        location = user_data["location"]["city"]
        return username, location
    else:
        raise Exception("API request failed or returned invalid data")

def main():
    try:
        # Attempt to fetch and process API data
        username, city = fetch_data_from_api()
        print(f"Username: {username}, City: {city}")
    except requests.RequestException as e:
        # Handle network-related errors
        print(f"Network error occurred: {e}")
    except KeyError as e:
        # Handle JSON parsing errors (missing keys)
        print(f"Error parsing API response: {e}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()