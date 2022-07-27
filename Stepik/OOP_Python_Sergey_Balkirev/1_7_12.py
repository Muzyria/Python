class Viber:
    msg_list = []

    @classmethod
    def add_message(cls, msg):
        """добавление нового сообщения в список сообщений;
        """
        cls.msg_list.append(msg)

    @classmethod
    def remove_message(cls, msg):
        """удаление сообщения из списка;
        """
        cls.msg_list.remove(msg)

    @classmethod
    def set_like(cls, msg):
        """поставить/убрать лайк для сообщения msg
        (если лайка нет то он ставится, если уже есть, то убирается);
        """
        if msg.fl_like == False:
            msg.fl_like = True
        else:
            msg.fl_like = False

    @classmethod
    def show_last_message(cls, value):
        """отображение последних сообщений;
        """
        for m in cls.msg_list[-value:]:
            print(m.text)

    @classmethod
    def total_messages(cls):
        """звращает общее число сообщений.
        """
        return len(cls.msg_list)


class Message:
    """позволяет создавать объекты-сообщения со следующим
    набором локальных свойств:
    text - текст сообщения (строка);
    fl_like - поставлен или не поставлен лайк у сообщения
    (булево значение True - если лайк есть и False - в противном
    случае, изначально False);
    P.S. Как хранить список сообщений, решите самостоятельно.
    """

    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
#Viber.remove_message(msg)   - ставим в комент, чтобы посмотреть проставился ли лайк для msg
for i in Viber.msg_list:
    print(i.__dict__)

Viber.show_last_message(2)
