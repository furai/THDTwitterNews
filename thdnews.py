import tweepy
import settings

if not hasattr(settings, 'ACCESS_TOKEN') and not hasattr(settings, "ACCESS_TOKEN_SECRET"):
	print "Settings are incomplete."
else:
	print "Everything seems to be fine, boss."

