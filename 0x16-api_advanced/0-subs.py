#!/usr/bin/python3
"""
Retrieves the number of subscribers for a given subreddit using the Reddit API.

This script uses the 'requests' library and implements basic error handling 
and rate limiting. It's important to use Reddit's API responsibly and respect 
their rate limits. Consider using official Reddit libraries like 'praw' for 
more advanced features and proper authentication.
"""

from requests import get
import time


def number_of_subscribers(subreddit):
  """
  Function that queries the Reddit API and returns the number of subscribers
  (not active users, total subscribers) for a given subreddit.

  Args:
      subreddit: The name of the subreddit (e.g., 'programming').

  Returns:
      The number of subscribers (integer) or 0 on error.
  """

  if subreddit is None or not isinstance(subreddit, str):
    return 0

  # Set a descriptive User-Agent string
  user_agent = {'User-agent': 'My Reddit Subscriber Scraper v1.0 (by your_username@example.com)'}
  url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

  # Add a small delay to avoid hitting rate limits
  time.sleep(1)  # Adjust delay as needed

  response = get(url, headers=user_agent)

  # Check the HTTP status code
  if response.status_code == 403:
    print("Error: Access forbidden. Received status code 403")
    return 0
  elif response.status_code != 200:
    print(f"Error: Received status code {response.status_code}")
    return 0

  # Attempt to parse the JSON response
  try:
    all_data = response.json()
  except ValueError as e:
    print(f"Error: Failed to parse JSON response - {e}")
    print(f"Response content: {response.text}")
    return 0

  # Safely extract the number of subscribers
  try:
    return all_data.get('data', {}).get('subscribers', 0)
  except Exception as e:
    print(f"Error: {e}")
    return 0


if __name__ == "__main__":
  import sys

  if len(sys.argv) < 2:
    print("Usage: python3 0-main.py <subreddit>")
  else:
    subreddit = sys.argv[1]
    subscribers = number_of_subscribers(subreddit)

    if subscribers > 0:
      print(f"Subreddit '{subreddit}' has {subscribers:,} subscribers.")  # Comma-separated formatting
    else:
      print(f"Error retrieving subscriber count for '{subreddit}'.")
#!/usr/bin/python3
"""
Retrieves the number of subscribers for a given subreddit using the Reddit API.

This script uses the 'requests' library and implements basic error handling 
and rate limiting. It's important to use Reddit's API responsibly and respect 
their rate limits. Consider using official Reddit libraries like 'praw' for 
more advanced features and proper authentication.
"""

from requests import get
import time


def number_of_subscribers(subreddit):
  """
  Function that queries the Reddit API and returns the number of subscribers
  (not active users, total subscribers) for a given subreddit.

  Args:
      subreddit: The name of the subreddit (e.g., 'programming').

  Returns:
      The number of subscribers (integer) or 0 on error.
  """

  if subreddit is None or not isinstance(subreddit, str):
    return 0

  # Set a descriptive User-Agent string
  user_agent = {'User-agent': 'My Reddit Subscriber Scraper v1.0 (by your_username@example.com)'}
  url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

  # Add a small delay to avoid hitting rate limits
  time.sleep(1)  # Adjust delay as needed

  response = get(url, headers=user_agent)

  # Check the HTTP status code
  if response.status_code == 403:
    print("Error: Access forbidden. Received status code 403")
    return 0
  elif response.status_code != 200:
    print(f"Error: Received status code {response.status_code}")
    return 0

  # Attempt to parse the JSON response
  try:
    all_data = response.json()
  except ValueError as e:
    print(f"Error: Failed to parse JSON response - {e}")
    print(f"Response content: {response.text}")
    return 0

  # Safely extract the number of subscribers
  try:
    return all_data.get('data', {}).get('subscribers', 0)
  except Exception as e:
    print(f"Error: {e}")
    return 0


if __name__ == "__main__":
  import sys

  if len(sys.argv) < 2:
    print("Usage: python3 0-main.py <subreddit>")
  else:
    subreddit = sys.argv[1]
    subscribers = number_of_subscribers(subreddit)

    if subscribers > 0:
      print(f"Subreddit '{subreddit}' has {subscribers:,} subscribers.")  # Comma-separated formatting
    else:
      print(f"Error retrieving subscriber count for '{subreddit}'.")