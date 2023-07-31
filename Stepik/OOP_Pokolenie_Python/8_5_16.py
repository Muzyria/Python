def limiter(limit, unique, lookup):
    instances = {}
    lookups = {}

    def wrapper(cls):
        def get_instance(*args, **kwargs):
            instance = cls(*args, **kwargs)
            lookups.setdefault('FIRST', instance)
            identifier = getattr(instance, unique)
            if len(instances) < limit:
                if identifier not in instances:
                    lookups['LAST'] = instances[identifier] = instance
                return instances[identifier]
            return instances.get(identifier) or lookups.get(lookup)

        return get_instance

    return wrapper
