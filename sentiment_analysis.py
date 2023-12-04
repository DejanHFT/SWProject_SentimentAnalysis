from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text_per_page = []
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text_per_page.append(page.get_text())
    return text_per_page

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def analyze_sentiment_nltk(text):
    # Create a SentimentIntensityAnalyzer object
    sid = SentimentIntensityAnalyzer()
    # Get the sentiment scores (positive, neutral, negative, and compound)
    sentiment_scores = sid.polarity_scores(text)
    # Extract the compound sentiment score
    compound_score = sentiment_scores['compound']
    # Return the compound sentiment score
    return compound_score

directory_path = r"C:\Users\dejan\Desktop\test stories"

# Iterate over each file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".pdf"):  # Adjust the file extension as needed
        file_path = os.path.join(directory_path, filename)

        # Extract text from the PDF
        text_per_page = extract_text_from_pdf(file_path)

        # Initialize variables for accumulating sentiment scores
        total_sentiment = 0
        total_sentiment_nltk = 0

        # Analyze sentiment for each page using TextBlob
        for page_num, page_text in enumerate(text_per_page, start=1):
            sentiment_score = analyze_sentiment(page_text)
            total_sentiment += sentiment_score

            # Analyze sentiment for each page using NLTK
            sentiment_score_nltk = analyze_sentiment_nltk(page_text)
            total_sentiment_nltk += sentiment_score_nltk

            # Print sentiment score for the current page
            print(f"Sentiment Score for {filename}, Page {page_num} (TextBlob): {sentiment_score}")
            print(f"Sentiment Score for {filename}, Page {page_num} (NLTK): {sentiment_score_nltk}")
            print()  # Add a newline for better readability between pages

        # Calculate average sentiment scores for the entire document
        average_sentiment = total_sentiment / len(text_per_page)
        average_sentiment_nltk = total_sentiment_nltk / len(text_per_page)

        # Print average sentiment scores for the entire document
        print(f"Average Sentiment Score for {filename} (TextBlob): {average_sentiment}")
        print(f"Average Sentiment Score for {filename} (NLTK): {average_sentiment_nltk}")
        print()  # Add a newline for better readability between files

# Example usage
# pdf_file_path = r"C:\Users\dejan\Desktop\1. The Tell Tale Heart  Author Edgar Allan Poe.pdf"
# document_text = extract_text_from_pdf(pdf_file_path)
# print(f"Document text: {document_text}")
#
# sentiment_score = analyze_sentiment(document_text)
# print(f"Sentiment Score: {sentiment_score}")
#
# sentiment_score2 = analyze_sentiment_nltk(document_text)
# print(f"Sentiment Score 2: {sentiment_score2}")

