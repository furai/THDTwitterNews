from twython import Twython
from collections import OrderedDict
import json
import time
import settings

if not hasattr(settings, 'ACCESS_TOKEN'):
	print "This is the first time you run this script. you need an access token for it to work."
	print "This is application authentication (no need to use user authentication as we will be only reading data from twitter)."
	twitter = Twython(settings.APP_KEY, settings.APP_SECRET, oauth_version=2)
	accToken = twitter.obtain_access_token()
	print "Edit your settings.py and add the line below to it:"
	print "ACCESS_TOKEN = \"%s\"" % accToken
else:
	twitter = Twython(settings.APP_KEY, access_token=settings.ACCESS_TOKEN)
	news = OrderedDict()
	for user in settings.USER:
		news.clear()
		i = 0
		user_timeline=twitter.get_user_timeline(screen_name=user, exclude_replies=True, include_rts=False)
		for tweet in user_timeline:
			if (settings.TAG in tweet['text'].lower()) and i < settings.NEWS_COUNT:
				i += 1
				news.update({u'tweet'+str(i):{u'text':tweet['text'],u'date':time.strftime("%Y-%m-%d",time.strptime(tweet['created_at'],"%a %b %d %H:%M:%S +0000 %Y"))}})
		filename = settings.PATH_TO_SAVE + '/' + user
		with open(filename, 'w') as outfile:
		    json.dump(news, outfile)
