
def find_keys(**kwargs) -> list[str]:
    return [k for k in sorted(kwargs.keys(), key=lambda x: x.lower()) if isinstance(kwargs[k], (list, tuple))]


print(find_keys(At=[4], awaited=(3,), aDobe=[5]))