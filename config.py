# defaualt config
import os 

class BaseConfig(object):
	DEBUG=False
	SECRET_KEY='\xa83\x14\x96\x1d\xf2o1\x8b\xa5r`\xf22\xe2\x9f\xdb7\x04\x90\x9ed\xeb\xa0'
	SQLALCHEMY_TRACK_MODIFICATIONS =False
	# SQLALCHEMY_DATABASE_URI = r'sqlite:///C:\Users\Chetan Baadkar\Documents\GitHub\flask_project\posts2.db'
	SQLALCHEMY_DATABASE_URI = 'postgres://cfuser:cfuser@localhost:5432/db_test'

	# SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
	DEBUG=True


class ProductionConfig(BaseConfig):
	DEBUG=False
	
	