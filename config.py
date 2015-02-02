WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
	{'name' : 'Google', 'url' : 'https://www.google.com/accounts/o8/id'},
	{'name' : 'Yahoo', 'url' : 'https://me.yahoo.com'},
	{'name' : 'AOL', 'url' : 'http://openid.aol.com/<username>'},
	{'name' : 'Flickr', 'url' : 'http://www.flickr.com/<username>'},
	{'name' : 'MyOpenID', 'url' : 'https://www.myopenid.com'}
	]
import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# email server
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'servertest1004'
MAIL_PASSWORD = 'jelenajelena'

# administrator list
ADMINS = ['servertest1004@gmail.com']

#pagination
POSTS_PER_PAGE = 3
USERS_PER_PAGE = 3

#full text search database
WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50

# Whoosh does not work on Heroku
WHOOSH_ENABLED = os.environ.get('HEROKU') is None