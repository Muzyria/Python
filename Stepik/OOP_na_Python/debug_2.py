class AttributeChecker:
    def __contains__(self, item):
        return item in self.__dict__

