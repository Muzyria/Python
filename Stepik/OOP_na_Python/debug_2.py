class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        cls._instance.log_level = "INFO"

        return cls._instance

    @classmethod
    def set_level(cls, x):
        if cls._instance:
            setattr(cls._instance, "log_level", x)
        else:
            raise ValueError('The instance has not been created')

    @staticmethod
    def get_logger():
        if not Logger._instance:
            Logger.__new__(Logger)
        return Logger._instance

try:
    logger_1 = Logger.set_level("DEBUG")
except ValueError as ex:
    print(ex)