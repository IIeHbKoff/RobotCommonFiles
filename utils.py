try:
    import csv
except ImportError:
    pass

import json

from common_files import Constants, Telemetry
from common_files.redis_lib import RedisLib


class Utils:
    def __init__(self):
        self.broker = RedisLib(host=Constants.REDIS_HOST, port=Constants.REDIS_PORT)
        self.telemetry = Telemetry()
        self.prev_packet = str()

    def calculate_points(self) -> list:
        pass

    def get_and_fill_telemetry(self):
        self.broker.pipeline()
        for param in self.telemetry.client_params:
            self.broker.get(key=param)
        list_of_answers = self.broker.execute()
        for index, param in enumerate(list_of_answers):
            if param is not None:
                self.telemetry.__setattr__(self.telemetry.client_params[index], param)

    def send_cmds(self):
        self.broker.pipeline()
        for param in self.telemetry.server_params:
            value = getattr(self.telemetry, param)
            if type(value) not in (str, int):
                value = json.dumps(value)
            self.broker.set(key=param, value=value)
        self.broker.execute()

    def get_and_fill_cmds(self):
        self.broker.pipeline()
        for param in self.telemetry.server_params:
            self.broker.get(key=param)
        list_of_answers = self.broker.execute()
        for index, param in enumerate(list_of_answers):
            setattr(self.telemetry, self.telemetry.server_params[index], json.loads(param.decode()))

    def send_telemetry(self):
        self.broker.pipeline()
        for param in self.telemetry.client_params:
            self.broker.set(key=param, value=getattr(self.telemetry, param))
        self.broker.execute()

    def connect(self):
        self.broker.connect()

    def disconnect(self):
        self.broker.close()


class FileManager:
    _instance = None
    _rows = dict()
    _file_name = "moods.csv"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FileManager, cls).__new__(cls)
        return cls._instance

    def read_file(self):
        with open(self._file_name, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter="|")
            self._rows = {row[0]: [int(i) for i in row[1].split(", ")] for row in reader}
        return self._rows

    def write_row(self, row: tuple):
        with open(self._file_name, "a") as csv_file:
            writer = csv.writer(csv_file, delimiter="|")
            self._rows[row[0]] = row[1]
            writer.writerow([row[0], str(row[1])[1:-1].replace("'", "")])

    def _rewrite_all_rows(self):
        with open(self._file_name, "w") as csv_file:
            writer = csv.writer(csv_file, delimiter="|")
            for key, value in self._rows.items():
                writer.writerow([key, str(value)[1:-1].replace("'", "")])

    def delete_row(self, row):
        if row:
            del self._rows[row]
            self._rewrite_all_rows()

    def edit_row(self, row: tuple):
        self._rows[row[0]] = row[1]
        self._rewrite_all_rows()
