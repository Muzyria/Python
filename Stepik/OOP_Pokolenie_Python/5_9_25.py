def limited_hash(left, right, hash_function=hash):
    def inner(obj):
        obj_hash = hash_function(obj)
        if left <= obj_hash <= right:
            return obj_hash
        elif obj_hash > right:
            return left + (obj_hash - right - 1) % (right - left + 1)
        else:
            return right - (left - obj_hash - 1) % (right - left + 1)

    return inner
