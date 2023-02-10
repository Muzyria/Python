class ObjList:
    def __init__(self, data: str):
        self.__data = ""
        self.data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) == str:
            self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        if type(obj) in (ObjList, type(None)):
            self.__prev = obj

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if type(obj) in (ObjList, type(None)):
            self.__next = obj


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        # self.obj_lst = []

    def add_obj(self, obj: object):
        obj.prev = self.tail

        if self.tail:
            self.tail.next = obj
        self.tail = obj

        if not self.head:
            self.head = obj


    def __get_obj_by_index(self, indx):
        h = self.head
        n = 0
        while h and n < indx:
            h = h.next
            n += 1
        return h

    def remove_obj(self, indx: int):
        obj = self.__get_obj_by_index(indx)
        if obj is None:
            return

        p, n = obj.prev, obj.next
        if p:
            p.next = n
        if n:
            p.prev = p

        if self.head == obj:
            self.head = n
        if self.tail == obj:
            self.tail = p

    def __len__(self):
        n = 0
        h = self.head
        while h:
            n += 1
            h = h.next
        return n

    def __call__(self, indx: int, *args, **kwargs):
        obj = self.__get_obj_by_index(indx)
        return obj.data if obj else None


if __name__ == '__main__':
    linked_lst = LinkedList()
    linked_lst.add_obj(ObjList("Sergey"))
    linked_lst.add_obj(ObjList("Balakirev"))
    linked_lst.add_obj(ObjList("Python"))
    linked_lst.remove_obj(2)
    linked_lst.add_obj(ObjList("Python ООП"))
    n = len(linked_lst)  # n = 3
    s = linked_lst(1)  # s = Balakirev
    print(n)
    print(s)
    print(linked_lst(0))
    print(linked_lst(1))
    print(linked_lst(2))
