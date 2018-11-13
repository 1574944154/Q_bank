import pymysql
import logging

from config import MYSQL_USER,MYSQL_HOST,MYSQL_DB,MYSQL_PW



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Mysql_db(object):

	def __init__(self):
		self.host = MYSQL_HOST
		self.user = MYSQL_USER
		self.password = MYSQL_PW
		self.db = MYSQL_DB

	def __get_conn(self):
		try:
			db = pymysql.connect(host=MYSQL_HOST, database=MYSQL_DB, user=MYSQL_USER, password=MYSQL_PW)
			return db
		except Exception as e:
			logger.info("error {}".format(e))


	def query(self, sql):
		db = self.__get_conn()
		cursor = db.cursor()
		try:
			cursor.execute(sql)
			db.commit()
			return cursor.fetchall()
		except Exception as e:
			print(e)
			db.rollback()
			return False
		finally:
			cursor.close()
			db.close()
