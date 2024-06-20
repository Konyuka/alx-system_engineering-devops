python
Copy code
#!/usr/bin/python3
"""
Function to query the Reddit API and return the number of subscribers for a given subreddit.
"""

from requests import get

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    # Check if subreddit is valid
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    # Set a custom User-Agent
    user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    # Construct the URL for the subreddit's about information
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    
    try:
        # Send GET request to Reddit API
        response = get(url, headers=user_agent)
        
        # Check if request was successful (status code 200)
        if response.status_code == 200:
            # Attempt to parse the JSON response
            all_data = response.json()
            
            # Safely extract the number of subscribers
            return all_data.get('data', {}).get('subscribers', 0)
        else:
            # Request was not successful, return 0
            return 0
    
    except Exception as e:
        # Handle any exceptions (e.g., network issues, JSON decoding errors)
        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 0-main.py <subreddit>")
    else:
        # Call the function with the subreddit name provided as argument
        print("{:d}".format(number_of_subscribers(sys.argv[1])))