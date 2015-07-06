# THD Twitter News
## Short description
Aim of this small project is to create an twitter rest app that will be run on crontab and will return json representation of users feed.
## Installation
- Install python and pip
- Install virtualenv `sudo pip install virtualenv`
- Clone this repository `git clone https://github.com/lucasgrzegorczyk/THDTwitterNews.git`
- cd into THDTwitterNews folder and create virtualenv `virtualenv --no-site-packages envthdnews`
- Activate virtualenv `source envthdnews/bin/activate`
- Install pip requirements `pip install -r requirements.txt`
- Copy settingy.py.example to settings.py and edit it
- Run tndnews for the first time `python thdnews.py`
- Follow instructions and copy access token to settings
- Add a crontab job
	- Example (will run cronjob every 15 minutes): `*/15 * * * * /path/to/your/cloned/repo/THDTwitterNews/envthdnews/bin/python /path/to/your/cloned/repo/THDTwitterNews/thdnews.py` 