def track_instances(cls):
    original_init = cls.__init__
    cls.instances = []

    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        cls.instances.append(self)

    cls.__init__ = new_init
    return cls
