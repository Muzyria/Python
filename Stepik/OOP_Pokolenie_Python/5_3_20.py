from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, version):
        self.version = version


