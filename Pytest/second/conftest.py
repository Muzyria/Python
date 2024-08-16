import pytest





@pytest.fixture(autouse=True)
def setup(request):
    print("START FIXTURE")
    request.cls.my = "MY"
    yield
    print("FINISH FIXTURE")
