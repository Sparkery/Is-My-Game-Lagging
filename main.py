#Aditya Ponukumati
#September 28, 2014
#Is LoL Lagging? Python Code

#
# Uses Twitter Search to compile the number of tweets containing LoL and lag for the current day
#

import tweepy
import datetime

print "Foxes!"

key = "key"
secret = "secret"

token = "tkey"
token_secret = "tsecret"

auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(token, token_secret)
api = tweepy.API(auth)

start = datetime.date.today().isoformat()

print api.me().name



##############
##############



print "\n\nTweets for", start, "\n"

results = api.search(q="(#leagueoflegends OR #league) AND (#lag OR lag)", since=start)
for result in results:
	print result.text, "\n"
print "\n", "There are", len(results), "results."

if len(results) <= 5:
	print "\nLikely not lagging."
elif len(results) > 5 and len(results) <= 10:
	print "\nPossibly lagging."
else:
	print "\nLagging."

#pub = api.home_timeline()
#for i in pub:
#        print str(i.__getstate__())

#public_tweets = api.public_timeline()
#for tweet in public_tweets:
#    print tweet.text
