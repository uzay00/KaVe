import tweepy
import csv #Import csv
auth = tweepy.auth.OAuthHandler('Consumer Key', 'Consumer Secret ')
auth.set_access_token('Access Token', 'Access Token Secret')

api = tweepy.API(auth)

# you need to create csv file to fill data
csvFile = open('datasetname.csv', 'a')

#we use data writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,
                           q = "keyword",
                           since = "2018-03-11",  
                           until = "2018-04-09",  
                           lang = "en").items():

    # way to save on csv
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print(tweet.created_at, tweet.text)
csvFile.close()
