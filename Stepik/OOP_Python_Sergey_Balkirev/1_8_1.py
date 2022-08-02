
class Server:
    buffer = []
    ip = []

    def __init__(self, ip=0):
        self.ip = ip + 1

    @classmethod
    def send_data(cls, data):
        pass

    @staticmethod
    def get_data():
        pass

    @staticmethod
    def get_ip():
        pass


class Router:
    buffer = []

    def __init__(self):
        pass

    @classmethod
    def link(cls, server):
        pass

    @classmethod
    def unlink(cls, server):
        pass

    @staticmethod
    def send_data():
        pass


class Data:
    data = ""
    ip = []

    def __init__(self, *args, ip):
        self.args = args
        self.ip = ip
