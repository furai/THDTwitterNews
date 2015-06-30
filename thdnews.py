from twython import Twython
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
	for user in settings.USER:
		user_timeline=twitter.get_user_timeline(screen_name=user, count=10, exclude_replies=True, include_rts=False)
		for tweet in user_timeline:
			print tweet + "\n"
