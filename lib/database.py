import MySQLdb
import time

query = """INSERT INTO data(`id`, `data`, `date`) VALUES (NULL, {}, NULL"""

class dbsetup:
	"""
	@basic setup for database connection
	"""
	def __init__(self, hostname, username, password, db):
		self.hostname = hostname
		self.username = username
		self.password = password
		self.db = db

	def connect(self):
		"""
		@return db object as after the connection to database established
		"""
		try:
			db = MySQLdb.connect(self.hostname, self.username, self.password, self.db)
		except Exception as err:
			raise(err)
		return db



