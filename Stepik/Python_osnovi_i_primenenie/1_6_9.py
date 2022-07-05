class LoggableList(Loggable, list):
    def append(self, x):
        self += [x]
        return self.log(x)