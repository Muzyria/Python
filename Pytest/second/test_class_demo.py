import pytest


class TestClassDemoInstance:
    value = 0


    @pytest.fixture(autouse=True)
    @classmethod
    def set_value(cls):
        cls.value = 5
        print()
        print(f"----- {cls.value}")
        print()

    def test_one(self):
        self.value = 1
        print()
        print(f"----- {self.value}")
        print()
        assert self.value == 1

    def test_two(self):
        print()
        print(f"----- {self.value}")
        print()
        assert self.value == 1
