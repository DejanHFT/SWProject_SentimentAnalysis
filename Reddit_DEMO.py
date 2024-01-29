import csv
import os
import time

import praw

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
    {'subreddit': 'movies', 'keyword': 'review'},
    {'subreddit': 'cooking', 'keyword': 'delicious'},
    {'subreddit': 'nature', 'keyword': 'beauty'},
    {'subreddit': 'philosophy', 'keyword': 'depression'},
    # {'subreddit': 'technology', 'keyword': 'innovation'},
    # {'subreddit': 'science', 'keyword': 'discovery'},
    # {'subreddit': 'worldnews', 'keyword': 'environment'},
    # {'subreddit': 'todayilearned', 'keyword': 'innovation'},
    # {'subreddit': 'space', 'keyword': 'astronomy'},
    # {'subreddit': 'askscience', 'keyword': 'technology'},
    # {'subreddit': 'history', 'keyword': 'insightful'},
    # {'subreddit': 'programming', 'keyword': 'coding'},
    # {'subreddit': 'business', 'keyword': 'entrepreneurship'},
    # {'subreddit': 'travel', 'keyword': 'adventure'},
    # {'subreddit': 'art', 'keyword': 'creativity'},
    # {'subreddit': 'education', 'keyword': 'learning'},
    # {'subreddit': 'writing', 'keyword': 'inspiration'},
    # {'subreddit': 'futurology', 'keyword': 'innovation'},
    # {'subreddit': 'desi-*-gn', 'keyword': 'creative'},
    {'subreddit': 'movies', 'keyword': 'critique'},
    # {'subreddit': 'food', 'keyword': 'tasty'},
    # {'subreddit': 'science', 'keyword': 'wonder'},
    # {'subreddit': 'technology', 'keyword': 'future'},
    # {'subreddit': 'history', 'keyword': 'insightful'},
    # {'subreddit': 'music', 'keyword': 'melody'},
    # {'subreddit': 'fitness', 'keyword': 'achievement'},
    # {'subreddit': 'gaming', 'keyword': 'strategy'},
    # {'subreddit': 'travel', 'keyword': 'exploration'},
    # {'subreddit': 'nature', 'keyword': 'serenity'},
    # {'subreddit': 'movies', 'keyword': 'cinema'},
    # {'subreddit': 'books', 'keyword': 'literary'},
    # {'subreddit': 'music', 'keyword': 'melancholy'},
    # {'subreddit': 'gaming', 'keyword': 'strategy'},
    # {'subreddit': 'fitness', 'keyword': 'wellness'},
    # {'subreddit': 'food', 'keyword': 'delicious'},
    # {'subreddit': 'technology', 'keyword': 'innovative'},
    {'subreddit': 'science', 'keyword': 'breakthrough'},
    # {'subreddit': 'travel', 'keyword': 'adventure'},
    # {'subreddit': 'history', 'keyword': 'historical'},
    # Add more subreddits and keywords as needed
]

# Set the number of posts to fetch for each subreddit/keyword combination
num_posts_per_subreddit_keyword = 2  # Adjust as needed

# Create a directory to store individual CSV files
output_directory = 'reddit_posts_DEMO/data'
os.makedirs(output_directory, exist_ok=True)

# Initialize variables for tracking progress
total_posts_saved = 0
start_time = time.time()

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

        # Generate a CSV file name based on the post ID, subreddit and keyword
        post_id = post.id
        csv_file_path = os.path.join(output_directory, f'{subreddit_name}_{keyword}_{post_id}.csv')

        # Write post details to the individual CSV file
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Title', 'Author', 'URL', 'Number of Comments', 'Upvotes', 'Text Content'])
            csv_writer.writerow([title, author, url, num_comments, upvotes, text_content])

        # Update progress information
        total_posts_saved += 1
        elapsed_time = time.time() - start_time

        # Print progress information
        print(f'Fetching post from subreddit "{subreddit_name}" using the keyword "{keyword}"...')
        print(f'Post saved to {csv_file_path}')
        print(f'Total posts saved: {total_posts_saved}, Total fetching time: {elapsed_time:.2f} seconds\n')

        # Add a sleep to avoid hitting API rate limits
        time.sleep(1)

# Print the final fetching process information
print(f'Fetching process finished. Total posts saved: {total_posts_saved}, Total fetching time: {elapsed_time:.2f} seconds')