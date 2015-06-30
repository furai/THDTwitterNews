from twython import Twython
import settings

if not hasattr(settings, 'ACCESS_TOKEN'):
	print "This is the first time you run this script. you need an access token for it to work."
	print "This is application authentication (no need to use user authentication as we will be only reading data from twitter)."
	twitter = Twython(settings.APP_KEY, settings.APP_SECRET, oauth_version=2)
	accToken = twitter.obtain_access_token()
	print "Edit your settings.py and add the line below to it:"
	print "ACCES_TOKEN = \"%s\"" % accToken
else:
	print "Everything seems to be fine, boss."
	twitter = Twython(APP_KEY, access_token=settings.ACCESS_TOKEN)
	search = twitter.search_gen('python')
	for result in search:
    	print result
