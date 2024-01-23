import csv
import os
import time

import praw

from nltk.sentiment import SentimentIntensityAnalyzer

# Set up your Reddit API credentials
client_id = 'ibAsUNj6QpjzZgeAV7EjZg'
client_secret = 'MXs2LBCI_jbeU1ai6JT5RzuzU9L6ZQ'
user_agent = 'SentimentAnalysis/1.0 by /u/31mide1mst'

# Authenticate with Reddit API
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

# Define a list of subreddits and corresponding keywords
subreddit_keywords = [
    {'subreddit': 'AskReddit', 'keyword': 'data science'},
    {'subreddit': 'AskReddit', 'keyword': 'AI'},
    {'subreddit': 'AskReddit', 'keyword': 'help'},
    {'subreddit': 'worldnews', 'keyword': 'war'},
    {'subreddit': 'worldnews', 'keyword': 'AI'},
    {'subreddit': 'todayilearned', 'keyword': 'AI'},
    {'subreddit': 'todayilearned', 'keyword': 'research'},
    {'subreddit': 'todayilearned', 'keyword': 'hobby'},
    {'subreddit': 'space', 'keyword': 'research'},
    {'subreddit': 'askscience', 'keyword': 'AI'},
    # Add more subreddits and keywords as needed
]

# Set the number of posts to fetch for each subreddit/keyword combination
num_posts_per_subreddit_keyword = 500  # Adjust as needed


# Create a directory to store individual CSV files
output_directory = 'reddit_posts/data'
os.makedirs(output_directory, exist_ok=True)

# Iterate through each subreddit/keyword combination
for entry in subreddit_keywords:
    subreddit_name = entry['subreddit']
    keyword = entry['keyword']

    # Fetch posts from the subreddit containing the keyword
    subreddit = reddit.subreddit(subreddit_name)
    posts = subreddit.search(keyword, limit=num_posts_per_subreddit_keyword)

    # Process and write each post to a separate CSV file
    for post in posts:
        title = post.title
        author = str(post.author)
        url = post.url
        num_comments = post.num_comments
        upvotes = post.score

        # Check if the post has text content
        if post.selftext:
            text_content = post.selftext
        else:
            text_content = "No text content"

        # Generate a CSV file name based on the post ID
        post_id = post.id
        csv_file_path = os.path.join(output_directory, f'post_{post_id}.csv')

        # Write post details to the individual CSV file
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Title', 'Author', 'URL', 'Number of Comments', 'Upvotes', 'Text Content'])
            csv_writer.writerow([title, author, url, num_comments, upvotes, text_content])

        print(f'Post saved to {csv_file_path}')

        # Add a sleep to avoid hitting API rate limits
        time.sleep(1)  # You can adjust the sleep duration as needed