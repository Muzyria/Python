import pytest


class TestClassDemoInstance:
    value = 0


    # @pytest.fixture(setup, request, autouse=True)
    # @classmethod
    # def set_value(cls):
    #     cls.value = 5
    #     print()
    #     print(request.cls.nodeid)
    #     print(f"----- {cls.value}")
    #     print()

    def test_one(self, setup, request):
        self.value = 1
        print()
        print(f"----- {self.value}")
        print(request.cls.my)
        # print(dir(request.cls))
        print(request.node.nodeid)
        print()
        assert self.value == 1

    def test_two(self):
        print()
        print(f"----- {self.value}")
        print()
        assert self.value == 0
