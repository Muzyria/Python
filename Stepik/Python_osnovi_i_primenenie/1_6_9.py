class LoggableList(list, Loggable):
    def append(self, x):
        self.log(x)
        return super().append(x)