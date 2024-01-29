from nltk.sentiment import SentimentIntensityAnalyzer
import os
import csv
import json
import glob


def analyze_sentiment_nltk(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)
    compound_score = sentiment_scores['compound']
    return compound_score


def analyze_sentiment_for_directory(directory_path):
    # Use glob to directly fetch all CSV files in the specified directory
    csv_files = glob.glob(os.path.join(directory_path, '*.csv'))

    # Create the .meta directory if it doesn't exist
    meta_directory = os.path.join(directory_path, '.meta')
    os.makedirs(meta_directory, exist_ok=True)

    # Iterate through CSV files
    for csv_file_path in csv_files:
        analyze_sentiment_for_csv(csv_file_path)


def analyze_sentiment_for_csv(csv_file_path):
    # Read the CSV file and analyze sentiment for each post
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
        # Skip header
        next(csv_file)
        # Read and analyze each row
        for row in csv.reader(csv_file):
            title = row[0]
            author = row[1]
            url = row[2]
            num_comments = row[3]
            upvotes = row[4]
            text_content = row[5]

            # Combine title and text content for sentiment analysis
            combined_text = f'{title} {text_content}' if text_content != "No text content" else title
            sentiment_scope = "Title & text content" if text_content != "No text content" else "Title content only"

            # Analyze sentiment using NLTK
            sentiment_score = analyze_sentiment_nltk(combined_text)

            # Get the base filename (including extension)
            base_filename = os.path.basename(csv_file_path)

            # Define the path for the JSON file with the exact same name as the CSV file
            json_file_path = os.path.join(directory_path, '.meta', f'{base_filename}.json')

            # Create the JSON structure
            json_data = {
                "title": title,
                "backlink": url,
                "language": "en",  # Modify as needed
                "classifications": ["reddit post"],  # Modify as needed
                "properties": {
                    "author": author,
                    "publication_year": 2024,  # Modify as needed
                    "external_link": url,
                    "sentiment_score": str(sentiment_score),  # Convert to string
                    "sentiment_label": get_sentiment_label(sentiment_score),  # Function to get sentiment label
                    "sentiment_scope": sentiment_scope  # Added sentiment_scope
                }
            }

            # Write JSON data to the file
            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                json.dump(json_data, json_file, ensure_ascii=False, indent=2)

            print(f'Sentiment data saved to {json_file_path}')


# Function to get sentiment label based on the sentiment score
def get_sentiment_label(sentiment_score):
    if sentiment_score > 0.5:
        return "very positive"
    elif 0.2 <= sentiment_score <= 0.5:
        return "positive"
    elif 0.05 <= sentiment_score < 0.2:
        return "slightly positive"
    elif -0.05 <= sentiment_score <= 0.05:
        return "neutral"
    elif -0.2 <= sentiment_score < -0.05:
        return "slightly negative"
    elif -0.5 <= sentiment_score < -0.2:
        return "negative"
    else:
        return "very negative"


# Usage:
directory_path = 'reddit_posts_DEMO/data'

analyze_sentiment_for_directory(directory_path)