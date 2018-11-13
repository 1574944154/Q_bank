from redis import Redis
from redis.connection import BlockingConnectionPool
from config import *


class Redis_db(object):

    def __init__(self):
        self.db = Redis(connection_pool=BlockingConnectionPool(host=REDIS_HOST, password=REDIS_PWD))

