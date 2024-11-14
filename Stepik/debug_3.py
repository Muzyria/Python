
def create_dict() -> callable:

    def inner(item) -> dict:
        inner.count += 1
        inner.cache[inner.count] = item
        return inner.cache
    inner.cache = {}
    inner.count = 0
    return inner
