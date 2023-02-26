import redis


class RedisConnect(object):
    __doc__ = """
    Connect pool for redis;
    """

    def __init__(self, redis_host="localhost", redis_port=6379, db=0, redis_password=None, max_connections=100, *args,
                 **kwargs):
        """
        Optimize Redis link pool
        :param redis_host: redis host for redis pool
        :param redis_port:redis port for redis pool
        :param db:redis db
        :param redis_password: redis password
        :param max_connections: max connections for redis.
        :param args: more
        :param kwargs: more
        """
        self.__redis_host = redis_host
        self.__redis_port = redis_port
        self.__redis_password = redis_password
        __redis_pool = redis.ConnectionPool(
            host=self.__redis_host,
            port=self.__redis_port,
            db=db,
            decode_responses=True,
            max_connections=max_connections,
            password=self.__redis_password,
            health_check_interval=30
                                  * args,
            **kwargs
        )
        self.redis_connect_pool = redis.Redis(connection_pool=__redis_pool, decode_responses=True)


if __name__ == '__main__':
    r = RedisConnect(db=2).redis_connect_pool
    r.rpush("test",str(0))
