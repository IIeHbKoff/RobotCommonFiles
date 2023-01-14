try:
    from redis import Redis
except ImportError:
    from libs.redis import Redis


class RedisLib:
    _instance = None
    _connection = None
    _opened_pipeline = None

    def __new__(cls, host: str, port: int):
        if cls._instance is None:
            cls._instance = super(RedisLib, cls).__new__(cls)
            cls._host = host
            cls._port = port
        return cls._instance

    def connect(self):
        self._connection: Redis = Redis(host=self._host, port=self._port)
        try:
            self._connection.connect()
        except AttributeError:
            pass

    def set(self, key, value):
        if self._opened_pipeline is not None:
            self._opened_pipeline.set(key, value)
        elif self._connection is not None:
            self._connection.set(key, value)

    def get(self, key):
        if self._opened_pipeline is not None:
            self._opened_pipeline.get(key)
        elif self._connection is not None:
            return self._connection.get(key).decode()

    def disconnect(self):
        self._connection = None

    def pipeline(self):
        if self._connection is not None:
            self._opened_pipeline = self._connection.pipeline(transaction=False)
        else:
            raise ConnectionError("No connect to Redis DB")

    def execute(self):
        if self._connection is not None:
            answer = self._opened_pipeline.execute()
            self._opened_pipeline = None
            return answer
