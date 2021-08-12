import boto3

#Using boto3 to call the Comprehend API
comprehendClient = boto3.client('comprehend', region_name = "us-east-1")

#lol ik its a dumb sentence
sampleText = "I am very happy in New York City, super excited to be working in the East, I can see the Statue of Liberty."

#Sentiment Analysis
sentiment = comprehendClient.detect_sentiment(Text = sampleText, LanguageCode = 'en') #API call for sentiment analysis
sentRes = sentiment['Sentiment'] #Positive, Neutral, or Negative
sentScore = sentiment['SentimentScore'] #Percentage of Positive, Neutral, and Negative
print(sentRes)
print(sentScore)