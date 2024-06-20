#!/usr/bin/python3

from requests import get

def number_of_subscribers(subreddit):
    
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        response = get(url, headers=user_agent)
        if response.status_code == 200:
            all_data = response.json()
            return all_data.get('data', {}).get('subscribers', 0)
        else:
            return 0
    
    except Exception as e:
        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 0-main.py <subreddit>")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))