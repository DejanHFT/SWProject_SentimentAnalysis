# SWProject_TF-IDF
Software Project with Mr. Stäbler. 
Repository of Group 1. 

# Insights about the example implementation 
- currently two sentiment analysis are being processed simultaneosly
- -> TextBlob and NLTK: From my experience suits better for our use case
- -> library is specialized for social media texts 

- In order to test out the implementation by yourself you just have to adjust the path accordingly to the path were the documents are located on your machine
- When you run the python script now the sentiment analysis is being processed page-wise 
- At the end the average sentiment is calculated and printed to the console as well before the next document gets processed 
- -> this is all adjustable; we can also analyse the sentiment of the whole text or split it up even further; maybe we can experiment here a little more

# Console output of example implementation 
Sentiment Score for 1. The Tell Tale Heart  Author Edgar Allan Poe.pdf, Page 1 (TextBlob): 0.01964699074074075
Sentiment Score for 1. The Tell Tale Heart  Author Edgar Allan Poe.pdf, Page 1 (NLTK): -0.9059

Sentiment Score for 1. The Tell Tale Heart  Author Edgar Allan Poe.pdf, Page 2 (TextBlob): 0.019392551892551894
Sentiment Score for 1. The Tell Tale Heart  Author Edgar Allan Poe.pdf, Page 2 (NLTK): -0.8978

Sentiment Score for 1. The Tell Tale Heart  Author Edgar Allan Poe.pdf, Page 3 (TextBlob): 0.02527233115468409
Sentiment Score for 1. The Tell Tale Heart  Author Edgar Allan Poe.pdf, Page 3 (NLTK): -0.9972

Sentiment Score for 1. The Tell Tale Heart  Author Edgar Allan Poe.pdf, Page 4 (TextBlob): 0.14812003968253967
Sentiment Score for 1. The Tell Tale Heart  Author Edgar Allan Poe.pdf, Page 4 (NLTK): -0.9045

Average Sentiment Score for 1. The Tell Tale Heart  Author Edgar Allan Poe.pdf (TextBlob): 0.0531079783676291
Average Sentiment Score for 1. The Tell Tale Heart  Author Edgar Allan Poe.pdf (NLTK): -0.92635

Sentiment Score for 2. The Monkeys Paw Author William W Jacobs.pdf, Page 1 (TextBlob): -0.007375992063492057
Sentiment Score for 2. The Monkeys Paw Author William W Jacobs.pdf, Page 1 (NLTK): 0.9006

Sentiment Score for 2. The Monkeys Paw Author William W Jacobs.pdf, Page 2 (TextBlob): 0.03856389146567717
Sentiment Score for 2. The Monkeys Paw Author William W Jacobs.pdf, Page 2 (NLTK): 0.9871

Sentiment Score for 2. The Monkeys Paw Author William W Jacobs.pdf, Page 3 (TextBlob): -0.04994949494949494
Sentiment Score for 2. The Monkeys Paw Author William W Jacobs.pdf, Page 3 (NLTK): -0.981

Sentiment Score for 2. The Monkeys Paw Author William W Jacobs.pdf, Page 4 (TextBlob): -0.001978454945322415
Sentiment Score for 2. The Monkeys Paw Author William W Jacobs.pdf, Page 4 (NLTK): 0.9573

Sentiment Score for 2. The Monkeys Paw Author William W Jacobs.pdf, Page 5 (TextBlob): -0.06577380952380955
Sentiment Score for 2. The Monkeys Paw Author William W Jacobs.pdf, Page 5 (NLTK): -0.9822

Sentiment Score for 2. The Monkeys Paw Author William W Jacobs.pdf, Page 6 (TextBlob): -0.026678004535147397
Sentiment Score for 2. The Monkeys Paw Author William W Jacobs.pdf, Page 6 (NLTK): -0.938

Average Sentiment Score for 2. The Monkeys Paw Author William W Jacobs.pdf (TextBlob): -0.018865310758598198
Average Sentiment Score for 2. The Monkeys Paw Author William W Jacobs.pdf (NLTK): -0.00936666666666667

Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 1 (TextBlob): 0.10035244816066731
Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 1 (NLTK): 0.9977

Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 2 (TextBlob): 0.13097422591821178
Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 2 (NLTK): 0.9977

Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 3 (TextBlob): 0.042457516339869286
Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 3 (NLTK): 0.9842

Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 4 (TextBlob): 0.12399200336700338
Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 4 (NLTK): -0.5394

Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 5 (TextBlob): 0.1607119236583522
Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 5 (NLTK): 0.9968

Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 6 (TextBlob): 0.04840796857463523
Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 6 (NLTK): -0.9855

Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 7 (TextBlob): 0.03721602182539683
Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 7 (NLTK): -0.9522

Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 8 (TextBlob): 0.11650321557728968
Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 8 (NLTK): 0.9975

Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 9 (TextBlob): 0.001331703166809549
Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 9 (NLTK): -0.9926

Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 10 (TextBlob): 0.04895650538092397
Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 10 (NLTK): -0.9934

Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 11 (TextBlob): 0.04396342083842083
Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 11 (NLTK): 0.7878

Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 12 (TextBlob): 0.003655278655278658
Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 12 (NLTK): 0.9861

Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 13 (TextBlob): -0.006168498168498174
Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 13 (NLTK): -0.9072

Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 14 (TextBlob): 0.16889709906951286
Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 14 (NLTK): -0.9635

Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 15 (TextBlob): 0.047263801353874896
Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 15 (NLTK): -0.9935

Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 16 (TextBlob): 0.11150575614861326
Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 16 (NLTK): -0.6257

Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 17 (TextBlob): -0.032780214458296646
Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 17 (NLTK): -0.9928

Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 18 (TextBlob): 0.03905560709132138
Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 18 (NLTK): -0.9939

Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 19 (TextBlob): 0.05309468694885364
Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 19 (NLTK): 0.9181

Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 20 (TextBlob): 0.03716731426366843
Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 20 (NLTK): -0.9975

Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 21 (TextBlob): 0.0014077367881715583
Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 21 (NLTK): 0.8142

Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 22 (TextBlob): 0.0634268133138615
Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 22 (NLTK): -0.9756

Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 23 (TextBlob): 0.04364628427128427
Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf, Page 23 (NLTK): -0.8963

Average Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf (TextBlob): 0.06021907035153155
Average Sentiment Score for 3. The Willows Author Algernon Blackwood.pdf (NLTK): -0.1882173913043478

# Questions for Mr. Stäbler:
- Is it okay if we process documents that are persisted on our local machine? E.g. 1000 pdf-documents, one of us has downloaded.
- -> Or is it neccessary to have a database where we persist our documents - so all our team members work on the "same documents"? Or would it just be a nice-to-have feature?
- Generally: What is the minimum amount of documents we have to process? Is it okay if we focus on mails, tales and short stories for our sentiment analysis? -> Background: Scientific Papers for example don't really have a sentiment.

-When to communicate to Moritz Platzer what kind of fields within the "Properties" we want to display on bigdata4biz? I think we will go for "sentiment_score" and "sentiment" but depending on our implementation we could add more things like "median_sentiment_score" or how accurate the score or sentiment is. For example: If the sentiment_score for each page alternates to heavily (-1 -> +1 -> 0,5 -> +1) we could add the disclaimer "not accurate"

-Any more questions from your group? 

# What is left to do to finish our first iteration: 
- Create a data lake with documents that meet our needs and meet the needs of Mr.Stäbler (see questions above)
- (think of the algorithm to calculate the sentiment; how to split up the text in a senseful way; what extras can you think of; what are best practices when analysing the sentiment score? (not really needed for our first prototype if you want to but would be really nice to have))
- Establish connection from our script to the data lake (very easy or already done with adjusting the path, if its okay that the documents are saved on our local machine)
- If we can save documents on local machine -> code to create .meta folder within that directory and to create the .json files within that .meta folder is missing
- If we can't save documents on our local machine -> access the documents and save them locally and then proceed with: "code to create .meta folder within that directory and to create the .json files within that .meta folder is missing"
- Upload the the documents via the bd4b-plugin -> maybe we can also implement that within our script. In order to not having to do it manually via command line

