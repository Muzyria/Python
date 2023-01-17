class Viber:
    list_msg = []

    def __init__(self, msg):
        self.msg = msg

    @staticmethod
    def add_message(msg):
        Viber.list_msg.append(msg)

    @staticmethod
    def remove_message(msg):
        Viber.list_msg.remove(msg)

    @staticmethod
    def set_like(msg):
        if msg.fl_like:
            msg.fl_like = False
        else:
            msg.fl_like = True

    @staticmethod
    def show_last_message(n: int):
        for i in range(n):
            print(Viber.list_msg[i])

    @staticmethod
    def total_messages():
        print(len(Viber.list_msg))


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like




