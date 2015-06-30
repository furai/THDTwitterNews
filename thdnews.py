from twython import Twython
import settings

if not hasattr(settings, 'ACCESS_TOKEN'):
	print "Settings are incomplete."
else:
	print "Everything seems to be fine, boss."

