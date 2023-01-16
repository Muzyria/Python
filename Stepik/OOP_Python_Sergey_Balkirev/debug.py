


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
        if not Viber.list_msg[Viber.list_msg.index(msg)].fl_like:
            Viber.list_msg[Viber.list_msg.index(msg)].fl_like = True
        else:
            Viber.list_msg[Viber.list_msg.index(msg)].fl_like = False

    @staticmethod
    def show_last_message(x):
        print(*Viber.list_msg[-x:])

    @staticmethod
    def total_messages():
        print(len(Viber.list_msg))


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like



msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)

Viber.total_messages()
#Viber.remove_message(msg)   - ставим в комент, чтобы посмотреть проставился ли лайк для msg
for i in Viber.list_msg:
    print(i.__dict__)

Viber.show_last_message(2)
