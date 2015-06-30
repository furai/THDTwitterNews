import tweepy
import settings

if not hasattr(settings, 'ACCESS_TOKEN'):
	print 'no access token'
